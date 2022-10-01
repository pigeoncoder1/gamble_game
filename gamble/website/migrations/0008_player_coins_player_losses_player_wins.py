# Generated by Django 4.0 on 2022-08-07 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0007_game_ownerchoice_game_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='coins',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='player',
            name='losses',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='player',
            name='wins',
            field=models.IntegerField(default=0),
        ),
    ]
