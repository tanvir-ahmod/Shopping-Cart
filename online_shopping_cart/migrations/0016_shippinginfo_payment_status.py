# Generated by Django 2.0.1 on 2018-03-31 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('online_shopping_cart', '0015_remove_shippinginfo_v_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='shippinginfo',
            name='payment_status',
            field=models.CharField(default='Pending', max_length=10),
        ),
    ]
