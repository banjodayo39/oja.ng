# Generated by Django 3.0.5 on 2020-04-22 03:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20200421_2040'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='qty_order_item',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='item',
            name='quantity',
            field=models.IntegerField(default=0),
        ),
    ]
