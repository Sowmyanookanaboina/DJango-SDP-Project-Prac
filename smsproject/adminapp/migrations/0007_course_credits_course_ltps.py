# Generated by Django 5.2.2 on 2025-07-17 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0006_facultycoursemapping'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='credits',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='course',
            name='ltps',
            field=models.CharField(default='0-0-0-0', max_length=10),
            preserve_default=False,
        ),
    ]
