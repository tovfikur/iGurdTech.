# Generated by Django 3.0.8 on 2020-07-30 04:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_usertoken'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usertoken',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='user.UserDetails'),
        ),
    ]
