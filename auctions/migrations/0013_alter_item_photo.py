# Generated by Django 4.0.4 on 2022-06-23 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0012_alter_item_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='photo',
            field=models.ImageField(blank=True, upload_to='images'),
        ),
    ]
