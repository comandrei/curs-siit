# Generated by Django 4.0.5 on 2022-06-21 16:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('curs', '0006_alter_student_an'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='student',
            unique_together={('nume', 'prenume')},
        ),
    ]