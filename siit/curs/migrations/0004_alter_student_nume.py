# Generated by Django 4.0.5 on 2022-06-21 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('curs', '0003_curs_student_an'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='nume',
            field=models.CharField(db_index=True, max_length=50),
        ),
    ]
