# Generated by Django 4.0.6 on 2022-08-08 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='class_section',
            field=models.CharField(choices=[('DS', 'Select the section'), ('A', 'SECTION A'), ('B', 'SECTION B'), ('C', 'SECTION C'), ('D', 'SECTION D'), ('E', 'SECTION E')], max_length=5),
        ),
        migrations.AlterField(
            model_name='student',
            name='standard',
            field=models.CharField(choices=[('DS', 'Select the class'), ('1st', 'FIRST'), ('2nd', 'SECOND'), ('3rd', 'THIRD'), ('4th', 'FOUR'), ('5th', 'FIFTH'), ('6th', 'SIXTH'), ('7th', 'SEVENTH'), ('8th', 'EIGTHTH'), ('9th', 'NINETH'), ('10th', 'TENTH'), ('11th', 'ELEVENTH'), ('12th', 'TWELVETH')], max_length=5),
        ),
        migrations.AlterField(
            model_name='student',
            name='stream',
            field=models.CharField(choices=[('DS', 'Select the Stream if you class greater than 10'), ('S', 'SCIENCE'), ('C', 'COMMERCE'), ('A', 'ARTS')], max_length=5),
        ),
    ]
