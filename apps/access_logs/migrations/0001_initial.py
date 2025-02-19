# Generated by Django 5.1.4 on 2024-12-19 04:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('credentials', '__first__'),
        ('devices', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccessLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('direction', models.CharField(choices=[('in', 'Вход'), ('out', 'Выход')], max_length=3)),
                ('result', models.CharField(choices=[('granted', 'Разрешено'), ('denied', 'Запрещено')], max_length=8)),
                ('additional_info', models.TextField(blank=True, null=True)),
                ('credential', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='logs', to='credentials.credential')),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='logs', to='devices.device')),
            ],
        ),
    ]
