# Generated by Django 2.2 on 2019-05-01 10:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course_lesson', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='complexity',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='module',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lessons', to='course_lesson.Module'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='lessons', to='course_lesson.Teacher'),
        ),
        migrations.AlterField(
            model_name='module',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='modules', to='course_lesson.Course'),
        ),
        migrations.AlterField(
            model_name='resource',
            name='lesson',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lessons', to='course_lesson.Lesson'),
        ),
    ]
