# Generated by Django 2.2 on 2019-05-01 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_lesson', '0003_auto_20190501_1542'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='next_course_id',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='course',
            name='previous_course_id',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='lesson',
            name='next_lesson_id',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='lesson',
            name='previous_lesson_id',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='module',
            name='next_module_id',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='module',
            name='previous_module_id',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
    ]