# Generated by Django 3.0.7 on 2020-07-08 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HomePage', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='prod_image',
            field=models.ImageField(default='', upload_to='./static/images'),
        ),
    ]
