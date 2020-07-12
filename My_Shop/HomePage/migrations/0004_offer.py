# Generated by Django 3.0.7 on 2020-07-11 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HomePage', '0003_auto_20200708_2042'),
    ]

    operations = [
        migrations.CreateModel(
            name='offer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('offer_name', models.CharField(default='', max_length=50)),
                ('offer_desc', models.CharField(default='', max_length=100)),
                ('offer_image', models.ImageField(default='', upload_to='images')),
            ],
        ),
    ]
