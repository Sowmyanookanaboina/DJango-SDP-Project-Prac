# Generated by Django 5.2.2 on 2025-07-16 16:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0005_course_program'),
    ]

    operations = [
        migrations.CreateModel(
            name='FacultyCourseMapping',
            fields=[
                ('mappingid', models.AutoField(primary_key=True, serialize=False)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminapp.course')),
                ('faculty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminapp.faculty')),
            ],
            options={
                'db_table': 'facultycoursemapping_table',
            },
        ),
    ]
