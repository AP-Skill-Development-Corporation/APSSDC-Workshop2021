from django.db import models

# Create your models here.
class CourseCategory(models.Model):
	ctitle = models.CharField(max_length=120)