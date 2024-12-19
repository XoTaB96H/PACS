from django.db import models


class AccessGroupDevices(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Role(models.Model):
    name = models.CharField(max_length=255, unique=True)
    username = models.CharField(max_length=255, unique=True, null=True, blank=True)
    password_hash = models.CharField(max_length=500, null=True, blank=True)
    description = models.CharField(max_length=500, null=True, blank=True)
    access_group_devices = models.ForeignKey('devices.AccessGroupDevices', null=True, blank=True,
                                             on_delete=models.SET_NULL)
    # access_group_devices = models.ForeignKey(AccessGroupDevices, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255, null=True, blank=True)
    photo = models.URLField(max_length=500, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    roles = models.ManyToManyField(Role, through='UserRole', related_name='users')

    def __str__(self):
        return f"{self.last_name} {self.first_name}"

class UserRole(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'role')

    def __str__(self):
        return f"{self.user} - {self.role}"
