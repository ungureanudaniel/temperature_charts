# Generated by Django 3.2.11 on 2022-01-10 16:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('temperature_data', '0003_delete_datainput'),
    ]

    operations = [
        migrations.CreateModel(
            name='DataInput',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='auth.user')),
                ('date', models.DateTimeField()),
                ('time', models.TimeField()),
                ('temp', models.IntegerField()),
                ('devices', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Dispozitive', to='temperature_data.device')),
            ],
        ),
    ]
