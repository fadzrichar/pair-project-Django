# Generated by Django 2.2.8 on 2019-12-12 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uhuy', '0006_auto_20191212_2225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='update_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
