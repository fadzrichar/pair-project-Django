# Generated by Django 2.2.8 on 2019-12-12 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Destination',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dest_image_path', models.CharField(blank=True, default='', max_length=255)),
                ('dest_name', models.CharField(blank=True, default='', max_length=255)),
                ('dest_desc', models.TextField(blank=True, default='', max_length=2000)),
                ('dest_checkin', models.DateField(auto_now_add=True, verbose_name='Check in')),
                ('dest_checkout', models.DateField(auto_now_add=True, verbose_name='Check out')),
                ('dest_price', models.IntegerField(default=0, max_length=10)),
                ('dest_rating', models.FloatField(default=0, max_length=4)),
            ],
        ),
    ]
