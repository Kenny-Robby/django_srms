# Generated by Django 5.0.1 on 2024-02-08 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('srmsApp', '0010_student_subject_result_gpa'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student_subject_result',
            name='gpa',
        ),
        migrations.AddField(
            model_name='result',
            name='gpa',
            field=models.FloatField(blank=True, null=True),
        ),
    ]