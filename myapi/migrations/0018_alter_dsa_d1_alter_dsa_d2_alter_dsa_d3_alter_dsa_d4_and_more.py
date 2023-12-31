# Generated by Django 4.2.5 on 2023-10-02 03:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0017_alter_dsa_d1_alter_dsa_d2_alter_dsa_d3_alter_dsa_d4_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dsa',
            name='d1',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dsa',
            name='d2',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dsa',
            name='d3',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dsa',
            name='d4',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dsa',
            name='d5',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='dsa',
            name='q1',
            field=models.URLField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='dsa',
            name='q2',
            field=models.URLField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='dsa',
            name='q3',
            field=models.URLField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='dsa',
            name='q4',
            field=models.URLField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='dsa',
            name='q5',
            field=models.URLField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='dsa',
            name='r1',
            field=models.URLField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='dsa',
            name='r2',
            field=models.URLField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='dsa',
            name='r3',
            field=models.URLField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='dsa',
            name='r4',
            field=models.URLField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='dsa',
            name='r5',
            field=models.URLField(blank=True, max_length=30, null=True),
        ),
    ]
