# Generated by Django 4.0.3 on 2022-04-05 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Client', '0003_rename_goal_person_goal_type_person_goal_weight'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='Age',
            field=models.IntegerField(max_length=10),
        ),
    ]
