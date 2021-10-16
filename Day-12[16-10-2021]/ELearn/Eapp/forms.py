# from django.contrib.auth.models import User
from Eapp.models import User
from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm
from django import forms
from Eapp.models import CourseCategory,SubCourse

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
		fields = ["ctitle","cimg"]
		widgets = {
		"ctitle":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter Course Title",
			})
		}

class SbCrl(forms.ModelForm):
	class Meta:
		model = SubCourse
		fields = ["crs","sbtitle","price","desc"]
		widgets = {
		"crs":forms.Select(attrs={
			"class":"form-control my-2",
			}),
		"sbtitle":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter SubCourse Name",
			}),
		"price":forms.NumberInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter Price",
			}),
		"desc":forms.Textarea(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter Description",
			"rows":5,
			}),
		}

class Pfupdf(forms.ModelForm):
	class Meta:
		model = User
		fields = ["first_name","last_name","email","age","gender","mobile","pfimg"]
		widgets = {
		"first_name":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter First Name",
			}),
		"last_name":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter Last Name",
			}),
		"email":forms.EmailInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter Your Email",
			}),
		"age":forms.NumberInput(attrs={
			"class":"form-control my-2",
			}),
		"gender":forms.Select(attrs={
			"class":"form-control my-2",
			}),
		"mobile":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter Your mobile number",
			}),
		}

class ChgPwd(PasswordChangeForm):
	old_password = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control my-2","placeholder":"Enter Old Password"}))
	new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control my-2","placeholder":"Enter New Password"}))
	new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control my-2","placeholder":"Enter Confirm New Password"}))
	class Meta:
		model = User
		fields ="__all__"

