# Generated by Django 4.2.5 on 2023-09-09 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0003_remove_dsa_questions_dsa_q1_dsa_q2_dsa_q3_dsa_q4_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dsa',
            name='q1',
            field=models.URLField(max_length=50),
        ),
        migrations.AlterField(
            model_name='dsa',
            name='q2',
            field=models.URLField(max_length=50),
        ),
        migrations.AlterField(
            model_name='dsa',
            name='q3',
            field=models.URLField(max_length=50),
        ),
        migrations.AlterField(
            model_name='dsa',
            name='q4',
            field=models.URLField(max_length=50),
        ),
        migrations.AlterField(
            model_name='dsa',
            name='q5',
            field=models.URLField(max_length=50),
        ),
    ]
