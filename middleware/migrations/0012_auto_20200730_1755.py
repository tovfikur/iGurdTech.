# Generated by Django 3.0.8 on 2020-07-30 17:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('middleware', '0011_auto_20200730_1751'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='transection',
            unique_together={('SellerWalletId', 'BuyerWalletId')},
        ),
    ]
