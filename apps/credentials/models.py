from django.db import models
from django.conf import settings

# Предполагаем, что User модель находится в apps.users.models
# Если она называется User и находится в том же проекте, можно импортировать:
# from apps.users.models import User
# или использовать get_user_model() если вы интегрируете с Django auth.
# В данном случае, так как мы писали пользовательскую модель, импорты будут выглядеть так:
from apps.users.models import User

class Credential(models.Model):
    CREDENTIAL_TYPE_CHOICES = (
        ('rfid', 'RFID'),
        ('mobile_id', 'Mobile ID'),
        ('qr', 'QR Code'),
        ('barcode', 'Barcode'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='credentials')
    credential_type = models.CharField(max_length=50, choices=CREDENTIAL_TYPE_CHOICES)
    credential_value = models.CharField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.user} - {self.credential_type}: {self.credential_value}"
