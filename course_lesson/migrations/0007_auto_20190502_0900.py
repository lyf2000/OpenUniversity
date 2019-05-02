# Generated by Django 2.2 on 2019-05-02 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_lesson', '0006_auto_20190501_1653'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lesson',
            name='next_id',
        ),
        migrations.RemoveField(
            model_name='lesson',
            name='previous_id',
        ),
        migrations.RemoveField(
            model_name='module',
            name='next_id',
        ),
        migrations.RemoveField(
            model_name='module',
            name='previous_id',
        ),
        migrations.AddField(
            model_name='course',
            name='queue_number',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='lesson',
            name='queue_number',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='module',
            name='queue_number',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]
