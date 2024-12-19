# Generated by Django 5.1.4 on 2024-12-19 04:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AccessGroupDevices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=255)),
                ('direction', models.CharField(choices=[('in', 'Вход'), ('out', 'Выход')], max_length=3)),
                ('device_type', models.CharField(choices=[('turnstile', 'Турникет'), ('door', 'Дверь')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='AccessGroupDevicesMap',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('access_group_devices', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='devices.accessgroupdevices')),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='devices.device')),
            ],
            options={
                'unique_together': {('access_group_devices', 'device')},
            },
        ),
    ]
