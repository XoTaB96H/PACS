from django.db import models

class Role(models.Model):
    name = models.CharField(max_length=255, unique=True)
    username = models.CharField(max_length=255, unique=True, null=True, blank=True)
    access_group_devices = models.ForeignKey('devices.AccessGroupDevices', null=True, blank=True, on_delete=models.SET_NULL)

    class Meta:
        verbose_name = "Роль"
        verbose_name_plural = "Роли"

    def __str__(self):
        return self.name

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255, null=True, blank=True)
    photo = models.URLField(max_length=500, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    # Прямое указание на роль (один пользователь - одна роль)
    role = models.ForeignKey(Role, null=True, blank=True, on_delete=models.SET_NULL, related_name='users')

    class Meta:
        verbose_name = "Сотрудник"
        verbose_name_plural = "Сотрудники"

    def __str__(self):
        return f"{self.last_name} {self.first_name}"
