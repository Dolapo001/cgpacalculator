# Generated by Django 4.2.2 on 2023-06-10 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calculator', '0002_alter_semester_grades'),
    ]

    operations = [
        migrations.AlterField(
            model_name='semester',
            name='course_units',
            field=models.CharField(default='', max_length=100),
        ),
    ]
