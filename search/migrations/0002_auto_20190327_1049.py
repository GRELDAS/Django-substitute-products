# Generated by Django 2.1.7 on 2019-03-27 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_fat',
            field=models.IntegerField(null=True),
        ),
    ]
