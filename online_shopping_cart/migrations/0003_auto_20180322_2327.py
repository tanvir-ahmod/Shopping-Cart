# Generated by Django 2.0.1 on 2018-03-22 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('online_shopping_cart', '0002_auto_20180322_2312'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='quantity',
            field=models.IntegerField(),
        ),
    ]
