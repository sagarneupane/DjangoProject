# Generated by Django 4.0.2 on 2022-02-18 02:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctionApp', '0010_rename_category_id_product_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='product',
            name='creator',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_bid_time',
            field=models.IntegerField(),
        ),
    ]
