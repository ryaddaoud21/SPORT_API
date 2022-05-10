# Generated by Django 4.0.3 on 2022-04-09 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Client', '0004_alter_person_age'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='Password',
        ),
        migrations.AlterField(
            model_name='person',
            name='Age',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='person',
            name='Email',
            field=models.EmailField(max_length=254, null=True),
        ),
    ]
