# Generated by Django 3.2.3 on 2021-06-17 19:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0008_auto_20210613_2108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicio',
            name='cliente',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='servicio',
            name='files',
            field=models.FileField(blank=True, null=True, upload_to='core/', verbose_name='Anexos'),
        ),
    ]