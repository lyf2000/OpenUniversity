from django.contrib import admin

from .models import *

admin.site.register(Teacher)
admin.site.register(Course)
admin.site.register(Module)
admin.site.register(Lesson)
admin.site.register(Resource)
