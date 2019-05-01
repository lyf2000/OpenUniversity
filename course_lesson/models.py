from django.db import models


# Create your models here.

class Teacher(models.Model):
	first_name = models.CharField(max_length=40)
	last_name = models.CharField(max_length=40)
	patronymic = models.CharField(max_length=40)
	photo_link = models.CharField(max_length=200)
	information = models.CharField(max_length=500)


class Course(models.Model):
	name = models.CharField(max_length=200)	
	description = models.CharField(max_length=800)
	complexity = models.PositiveSmallIntegerField(default=0)
	language = models.CharField(max_length=50)
	video_link = models.CharField(max_length=200)


class Module(models.Model):
	name = models.CharField(max_length=200)	
	course = models.ForeignKey(Course, on_delete=models.CASCADE)


class Lesson(models.Model):
	name = models.CharField(max_length=150)
	video_link = models.CharField(max_length=200)
	description = models.CharField(max_length=500)
	module = models.ForeignKey(Module, on_delete=models.CASCADE)
	teacher = models.ForeignKey(Teacher, on_delete=models.PROTECT)


class Resource(models.Model):
	name = models.CharField(max_length=150)
	resource_link = models.CharField(max_length=250)
	lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)