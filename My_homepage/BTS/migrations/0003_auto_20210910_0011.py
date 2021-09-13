# Generated by Django 3.2.7 on 2021-09-09 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BTS', '0002_albums'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artist',
            name='appearance',
        ),
        migrations.AddField(
            model_name='artist',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
    ]
