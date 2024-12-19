from django.db import models

class Device(models.Model):
    DIRECTION_CHOICES = (
        ('in', 'Вход'),
        ('out', 'Выход'),
    )

    DEVICE_TYPE_CHOICES = (
        ('turnstile', 'Турникет'),
        ('door', 'Дверь'),
    )

    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    direction = models.CharField(max_length=3, choices=DIRECTION_CHOICES)
    device_type = models.CharField(max_length=50, choices=DEVICE_TYPE_CHOICES)

    class Meta:
        verbose_name = "Устройство"
        verbose_name_plural = "Устройства"

    def __str__(self):
        return f"{self.name} ({self.location})"


class AccessGroupDevices(models.Model):
    name = models.CharField(max_length=255)
    # Прямое M2M-отношение к Device без отдельной промежуточной модели
    devices = models.ManyToManyField(Device, related_name='device_groups', blank=True)

    class Meta:
        verbose_name = "Группа устройств"
        verbose_name_plural = "Группы устройств"

    def __str__(self):
        return self.name
