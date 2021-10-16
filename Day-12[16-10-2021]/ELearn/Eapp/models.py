from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
	t = {
		('F','Female'),('M','Male')
		}
	y = {(1,'Student'),(2,'Instructor')}
	age = models.IntegerField(default=18)
	gender = models.CharField(choices=t,max_length=10)
	mobile = models.CharField(max_length=11)
	pfimg = models.ImageField(upload_to='Profileimage/',default="profile.png")
	usrole = models.IntegerField(choices=y,default=1)

class CourseCategory(models.Model):
	ctitle = models.CharField(max_length=120)
	cimg = models.ImageField(upload_to='CourseImages/',default="course.png")
	usd = models.ForeignKey(User,on_delete=models.CASCADE)

	def __str__(self):
		return self.ctitle

class SubCourse(models.Model):
	sbtitle = models.CharField(max_length=100)
	price = models.DecimalField(max_digits=8,decimal_places=2)
	desc = models.TextField(max_length=200)
	crs = models.ForeignKey(CourseCategory,on_delete=models.CASCADE)

	def __str__(self):
		return str(self.crs)+" "+self.sbtitle
