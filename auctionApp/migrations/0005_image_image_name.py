# Generated by Django 4.0.2 on 2022-02-17 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctionApp', '0004_image_user_alter_image_image_path'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='image_name',
            field=models.CharField(default='Sorry', max_length=100),
        ),
    ]