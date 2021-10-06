from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def sample(self):
	return HttpResponse('<script>alert("Hi")</script>Hi welcome...')

def dsname(self,name):
	return HttpResponse('<h1>Hi Welcome {}</h1>'.format(name))

def fname(s,age,name):
	return HttpResponse('<h1>Hi Welcome <br>Your name is: <span style="color:green">{}</span><br> Your age is:<span style="color:red">{}</span></h1>'.format(name,age))

def emp(ds,fname,lname,sal):
	return HttpResponse("<html><h1>Hi Welcome Employee<br>Your First Name is: <span id='fn'>{}</span><br>Your Last Name is: {}<br>Your Salary is:{}</h1></html>".format(fname,lname,sal)) 

def empdetials(request,empname,sal):
	return render(request,'demo.html',{'e':empname,'s':sal})

def dname(request,sname):
	g = {'sn':sname}
	return render(request,'ty/fa.html',g)

def stname(request,stname,year,branch):
	return render(request,'ty/std.html',{'sn':stname,'y':year,'b':branch})

def regis(request):
	if request.method == "POST":
		name = request.POST['sname']
		year = request.POST['syear']
		return render(request,'ty/display.html',{'s':name,'y':year})
	return render(request,'ty/register.html')

def index(request):
	return render(request,'ty/index.html')

def about(request):
	return render(request,'ty/about.html')

def contact(request):
	return render(request,'ty/contact.html')

def sample(request):
	return render(request,'ty/sample.html')