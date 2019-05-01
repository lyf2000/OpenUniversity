from django.db import models


# Create your models here.

class Teacher(models.Model):
	first_name = models.CharField(max_length=40)
	last_name = models.CharField(max_length=40)
	patronymic = models.CharField(max_length=40)
	photo_link = models.CharField(max_length=200)
	information = models.CharField(max_length=500)

	def __str__(self):
		return f'{self.first_name}'


class Course(models.Model):
	name = models.CharField(max_length=200)	
	description = models.CharField(max_length=800)
	complexity = models.PositiveSmallIntegerField(default=0)
	language = models.CharField(max_length=50)
	video_link = models.CharField(max_length=200)

	def __str__(self):
		return f'{self.name}'

class Module(models.Model):
	name = models.CharField(max_length=200)	
	course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='modules')

	previous_id = models.PositiveSmallIntegerField(blank=True,null=True)
	next_id = models.PositiveSmallIntegerField(blank=True,null=True)

	def __str__(self):
		return f'{self.name} module from {self.course.name}'

class Lesson(models.Model):

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.change_video_link()

	name = models.CharField(max_length=150)
	video_link = models.CharField(max_length=200)
	description = models.CharField(max_length=500)
	module = models.ForeignKey(Module, on_delete=models.CASCADE, related_name='lessons')
	teacher = models.ForeignKey(Teacher, on_delete=models.PROTECT, related_name='lessons')

	previous_id = models.PositiveSmallIntegerField(blank=True, null=True)
	next_id = models.PositiveSmallIntegerField(blank=True, null=True)

	def change_video_link(self):
		link = self.video_link
		if '=' in link:
			link = link[link.index('=')+1:]
			head = 'https://www.youtube.com/embed/'
			self.video_link = head + link
			self.save()

	def __str__(self):
		return f'{self.name} lesson from {self.module.name} module'

class Resource(models.Model):


	name = models.CharField(max_length=150)
	resource_link = models.CharField(max_length=250)
	lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='resources')

	def __str__(self):
		return f'{self.name} resource'

