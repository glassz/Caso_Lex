# Generated by Django 3.2.4 on 2021-06-28 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_auto_20210628_1602'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicio',
            name='phone',
            field=models.CharField(blank=True, max_length=12, null=True, verbose_name='Telefono'),
        ),
    ]
