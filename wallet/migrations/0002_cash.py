# Generated by Django 3.0.8 on 2020-07-29 10:38

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cash',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PhoneNumber', phonenumber_field.modelfields.PhoneNumberField(default='+8801796693300', max_length=128, region=None)),
                ('TrxId', models.CharField(max_length=64, unique=True)),
            ],
        ),
    ]
