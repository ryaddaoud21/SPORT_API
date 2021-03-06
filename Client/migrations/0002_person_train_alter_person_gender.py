# Generated by Django 4.0.3 on 2022-03-26 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Client', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='Train',
            field=models.FloatField(help_text='number of times do you train per week', max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='Gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default='M', max_length=10),
        ),
    ]
