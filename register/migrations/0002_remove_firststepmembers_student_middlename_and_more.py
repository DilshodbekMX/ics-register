# Generated by Django 4.0.3 on 2022-04-06 08:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='firststepmembers',
            name='student_middlename',
        ),
        migrations.RemoveField(
            model_name='secondstepmembers',
            name='student_middlename',
        ),
    ]
