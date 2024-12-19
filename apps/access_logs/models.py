from django.db import models
from apps.credentials.models import Credential
from apps.devices.models import Device

class AccessLog(models.Model):
    DIRECTION_CHOICES = (
        ('in', 'Вход'),
        ('out', 'Выход'),
    )
    RESULT_CHOICES = (
        ('granted', 'Разрешено'),
        ('denied', 'Запрещено'),
    )

    credential = models.ForeignKey(Credential, on_delete=models.CASCADE, related_name='logs')
    device = models.ForeignKey(Device, on_delete=models.CASCADE, related_name='logs')
    timestamp = models.DateTimeField(auto_now_add=True)
    direction = models.CharField(max_length=3, choices=DIRECTION_CHOICES)
    result = models.CharField(max_length=8, choices=RESULT_CHOICES)
    additional_info = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.timestamp}: {self.credential} - {self.device} [{self.result}]"
