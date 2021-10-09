from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from Eapp.models import CourseCategory

class UsReg(UserCreationForm):
	password1 = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control my-2","placeholder":"Enter Password"}))
	password2 = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control my-2","placeholder":"Enter Confirmation Password"}))
	class Meta:
		model = User
		fields = ["username"]
		widgets = {
		"username":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter Username"
			})
		}

class Crcty(forms.ModelForm):
	class Meta:
		model = CourseCategory
		fields = ["ctitle"]
		widgets = {
		"ctitle":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter Course Title",
			})
		}



