# Generated by Django 2.2 on 2019-05-01 13:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course_lesson', '0004_auto_20190501_1624'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='next_course_id',
        ),
        migrations.RemoveField(
            model_name='course',
            name='previous_course_id',
        ),
    ]