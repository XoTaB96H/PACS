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

    name = models.CharField(max_length=255)  # "Турникет №1"
    location = models.CharField(max_length=255)  # "Главный вход"
    direction = models.CharField(max_length=3, choices=DIRECTION_CHOICES)
    device_type = models.CharField(max_length=50, choices=DEVICE_TYPE_CHOICES)

    def __str__(self):
        return f"{self.name} ({self.location})"


class AccessGroupDevices(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class AccessGroupDevicesMap(models.Model):
    access_group_devices = models.ForeignKey(AccessGroupDevices, on_delete=models.CASCADE)
    device = models.ForeignKey(Device, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.access_group_devices.name} -> {self.device.name}"

    class Meta:
        unique_together = ('access_group_devices', 'device')
