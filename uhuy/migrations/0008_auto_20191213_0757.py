# Generated by Django 2.2.8 on 2019-12-13 00:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uhuy', '0007_auto_20191212_2257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='picture',
            field=models.ImageField(upload_to='img/'),
        ),
    ]
