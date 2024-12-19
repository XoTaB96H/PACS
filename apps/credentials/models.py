from django.db import models
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

    class Meta:
        verbose_name = "Идентификатор"
        verbose_name_plural = "Идентификаторы"

    def __str__(self):
        return f"{self.user} - {self.get_credential_type_display()}: {self.credential_value}"
