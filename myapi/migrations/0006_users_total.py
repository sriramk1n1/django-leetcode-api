# Generated by Django 4.2.5 on 2023-09-09 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0005_remove_dsa_id_alter_dsa_weekno'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='total',
            field=models.IntegerField(null=True),
        ),
    ]
