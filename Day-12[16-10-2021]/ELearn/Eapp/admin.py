from django.contrib import admin
from Eapp.models import CourseCategory,SubCourse,User
# Register your models here.

admin.site.register(CourseCategory)
admin.site.register(SubCourse)
admin.site.register(User)