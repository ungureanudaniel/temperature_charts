# Generated by Django 3.2.11 on 2022-01-12 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('temperature_data', '0007_auto_20220112_1031'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='datainput',
            name='devices',
        ),
        migrations.AddField(
            model_name='datainput',
            name='devices',
            field=models.CharField(default='a', max_length=255),
            preserve_default=False,
        ),
    ]
