# Generated by Django 4.2.5 on 2023-09-10 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0009_visits'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='week',
            field=models.IntegerField(default=0),
        ),
    ]
