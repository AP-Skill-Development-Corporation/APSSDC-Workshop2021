from django.db import models

# Create your models here.
class EmployeeDetails(models.Model):
	ename = models.CharField(max_length=100)
	eage = models.IntegerField()
	eusname = models.CharField(max_length=120)
	epwd = models.CharField(max_length=120)
	eemail = models.EmailField(max_length=120)

	def __str__(self):
		return self.ename