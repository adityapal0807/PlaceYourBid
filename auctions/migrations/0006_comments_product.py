# Generated by Django 4.0.4 on 2022-06-20 06:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0005_comments'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='product',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='auctions.item'),
            preserve_default=False,
        ),
    ]
