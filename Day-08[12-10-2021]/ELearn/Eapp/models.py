from django.db import models

# Create your models here.
class CourseCategory(models.Model):
	ctitle = models.CharField(max_length=120)

	def __str__(self):
		return self.ctitle

class SubCourse(models.Model):
	sbtitle = models.CharField(max_length=100)
	price = models.DecimalField(max_digits=8,decimal_places=2)
	desc = models.TextField(max_length=200)
	crs = models.ForeignKey(CourseCategory,on_delete=models.CASCADE)

