# Generated by Django 5.2.2 on 2025-06-15 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0002_alter_course_department'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='academicyear',
            field=models.CharField(choices=[('2023-24', '2023-24'), ('2022-23', '2022-23')], max_length=20),
        ),
        migrations.AlterField(
            model_name='course',
            name='department',
            field=models.CharField(choices=[('CSE(R)', 'CSE(REGULAR)'), ('CSE(H)', 'CSE(HONORS)'), ('CSIT', 'CSIT')], max_length=100),
        ),
        migrations.AlterField(
            model_name='course',
            name='semester',
            field=models.CharField(choices=[('EVEN', 'EVEN'), ('ODD', 'ODD')], max_length=10),
        ),
    ]
