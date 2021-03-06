# Generated by Django 3.0.8 on 2020-07-28 19:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WalletDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Cash', models.IntegerField()),
                ('TotalTransection', models.IntegerField()),
                ('TotalWithdraw', models.IntegerField()),
                ('LastActive', models.DateTimeField(auto_now_add=True)),
                ('userId', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='user.UserDetails')),
            ],
        ),
    ]
