# Generated by Django 5.0.1 on 2024-02-07 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('srmsApp', '0006_student_birthdate'),
    ]

    operations = [
        migrations.AddField(
            model_name='student_subject_result',
            name='grade',
            field=models.CharField(blank=True, choices=[('A', 'A'), ('B+', 'B+'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('F', 'F')], max_length=2, null=True),
        ),
        migrations.AddField(
            model_name='student_subject_result',
            name='grade_point',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
