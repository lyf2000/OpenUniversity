from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class CustomUser(User):
	data_joined = models.DateTimeField()

	def __str__(self):
		return f'{self.username}'