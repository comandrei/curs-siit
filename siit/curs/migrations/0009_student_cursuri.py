# Generated by Django 4.0.5 on 2022-06-21 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('curs', '0008_question_alter_student_options_choice'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='cursuri',
            field=models.ManyToManyField(to='curs.curs'),
        ),
    ]