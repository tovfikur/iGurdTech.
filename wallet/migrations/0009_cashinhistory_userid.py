# Generated by Django 3.0.8 on 2020-07-30 10:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0008_remove_cashinhistory_userid'),
    ]

    operations = [
        migrations.AddField(
            model_name='cashinhistory',
            name='userId',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='wallet.WalletDetails'),
        ),
    ]
