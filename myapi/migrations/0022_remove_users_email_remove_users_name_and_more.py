# Generated by Django 4.2.7 on 2023-11-08 13:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0021_delete_visits'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='email',
        ),
        migrations.RemoveField(
            model_name='users',
            name='name',
        ),
        migrations.RemoveField(
            model_name='users',
            name='totalweek',
        ),
        migrations.RemoveField(
            model_name='users',
            name='week',
        ),
    ]
