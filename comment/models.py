from django.db import models
from course_lesson.models import Lesson, Course
from signin_signup.models import CustomUser
# Create your models here.


class Comment(models.Model):
	comment_text = models.CharField(max_length=400)
	date = models.DateTimeField('date published')
	user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
	lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, null=True)
	course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True)