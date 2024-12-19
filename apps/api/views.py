from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q
from apps.credentials.models import Credential
from apps.devices.models import Device, AccessGroupDevicesMap
from apps.access_logs.models import AccessLog
from apps.users.models import UserRole, Role
from .serializers import CheckAccessSerializer

class CheckAccessView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = CheckAccessSerializer(data=request.data)
        if serializer.is_valid():
            credential_value = serializer.validated_data.get('credential_value')
            device_id = serializer.validated_data.get('device_id')

            # Проверяем наличие пропуска
            try:
                credential = Credential.objects.select_related('user').get(credential_value=credential_value)
            except Credential.DoesNotExist:
                # Нет пропуска - доступ запрещен
                self._log_access(None, device_id, 'out', 'denied', additional_info='Credential not found')
                return Response({"result": "denied", "reason": "Credential not found"}, status=status.HTTP_200_OK)

            # Проверяем активность пропуска и пользователя
            if not credential.is_active or not credential.user.is_active:
                self._log_access(credential, device_id, 'out', 'denied', additional_info='Credential or user inactive')
                return Response({"result": "denied", "reason": "Inactive credential or user"}, status=status.HTTP_200_OK)

            # Проверяем принадлежность устройства группе, доступной пользователю
            # Получаем роли пользователя
            user_roles = credential.user.roles.all()  # ManyToMany через UserRole
            # Собираем все группы устройств, доступные по ролям
            access_group_ids = [r.access_group_devices_id for r in user_roles if r.access_group_devices_id]

            if not access_group_ids:
                # Нет доступных групп, значит нет доступа
                self._log_access(credential, device_id, 'out', 'denied', additional_info='No device groups assigned')
                return Response({"result": "denied", "reason": "No device groups for user"}, status=status.HTTP_200_OK)

            # Проверяем, входит ли устройство в одну из групп
            device_in_group = AccessGroupDevicesMap.objects.filter(
                access_group_devices_id__in=access_group_ids,
                device_id=device_id
            ).exists()

            if not device_in_group:
                # Устройство не в доступной группе
                self._log_access(credential, device_id, 'out', 'denied', additional_info='Device not in accessible groups')
                return Response({"result": "denied", "reason": "Device not accessible for user"}, status=status.HTTP_200_OK)

            # Всё ок, доступ разрешён
            # Для direction можем использовать device.direction, но в запросе не обязательно передавать
            # Предположим, что direction берем из устройства
            try:
                device = Device.objects.get(pk=device_id)
                direction = device.direction
            except Device.DoesNotExist:
                # Если устройство не найдено, логируем denied (хотя на практике мы уже знаем что оно есть, просто на всякий случай)
                self._log_access(credential, device_id, 'out', 'denied', additional_info='Device not found')
                return Response({"result": "denied", "reason": "Device not found"}, status=status.HTTP_200_OK)

            self._log_access(credential, device_id, direction, 'granted')
            return Response({"result": "granted"}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def _log_access(self, credential, device_id, direction, result, additional_info=None):
        # Логируем событие
        # credential может быть None если пропуск не найден
        from apps.devices.models import Device
        device = Device.objects.filter(pk=device_id).first()
        AccessLog.objects.create(
            credential=credential if credential else None,
            device=device if device else None,
            direction=direction,
            result=result,
            additional_info=additional_info
        )
