# Generated by Django 3.0.8 on 2020-07-29 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0004_cashhistory_amount'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CashHistory',
            new_name='CashInHistory',
        ),
        migrations.AlterField(
            model_name='walletdetails',
            name='Cash',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='walletdetails',
            name='TotalTransection',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='walletdetails',
            name='TotalWithdraw',
            field=models.IntegerField(default=0),
        ),
    ]
