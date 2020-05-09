# Generated by Django 3.0.5 on 2020-04-19 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='category',
            field=models.CharField(choices=[('G', 'GRAINS'), ('V', 'VEGETABLE'), ('F', 'FAT_AND_OIL'), ('C', 'CUDIMENTS')], default='V', max_length=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='item',
            name='label',
            field=models.CharField(choices=[('P', 'primary'), ('S', 'secondary'), ('D', 'danger')], default='P', max_length=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='item',
            name='price',
            field=models.FloatField(default=0.0, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='item',
            name='quantity',
            field=models.IntegerField(default=0, max_length=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='item',
            name='total_price',
            field=models.FloatField(default=0.0, max_length=10),
            preserve_default=False,
        ),
    ]