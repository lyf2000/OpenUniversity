from django.db import models
from course_lesson.models import Module
from course_lesson.models import Course
from django.utils import timezone


# Create your models here.


class Test(models.Model):
	test_name = models.CharField(max_length=100) #LENGTH
	module = models.OneToOneField(Module, on_delete=models.CASCADE)


class Question(models.Model):
	question_text = models.TextField(max_length=300)
	correct_answer = models.OneToOneField('Answer', on_delete=models.CASCADE, related_name = 'question_correct_answer', null=True, blank=True)
	test = models.ForeignKey('Test', on_delete=models.CASCADE, related_name = 'questions')


class Answer(models.Model):
	answer_text = models.CharField(max_length=300)
	question = models.ForeignKey('Question', on_delete=models.CASCADE)


class MyTest(models.Model):
	test = models.ForeignKey('Test', on_delete=models.CASCADE, related_name='mytest_test', null=True)
	date = models.DateTimeField(default = timezone.now)
	module = models.ForeignKey(Module, on_delete=models.CASCADE, related_name='mytest_user')


class QuestionResult(models.Model):
	question = models.ForeignKey('Question', on_delete=models.CASCADE, related_name='question_results')
	mytest = models.ForeignKey('MyTest', on_delete=models.CASCADE, related_name='mytests')
	selected_answer = models.ForeignKey('Answer', on_delete=models.CASCADE, related_name='selected_answer')