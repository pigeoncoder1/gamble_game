# Generated by Django 4.0 on 2022-08-06 14:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='cat',
        ),
    ]
