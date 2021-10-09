from django.shortcuts import render,redirect
from django.http import HttpResponse
from Employee.models import EmployeeDetails

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

def register(request):
	return render(request,'ty/eregister.html')

def operations(request):
	k = EmployeeDetails.objects.all()
	if request.method == "POST":
		u = request.POST['us']
		p = request.POST['pd']
		n = request.POST['na']
		a = request.POST['ag']
		e = request.POST['em']
		cr = EmployeeDetails(ename=n,eage=a,eusname=u,epwd=p,eemail=e)
		cr.save()
		return redirect('/')
	return render(request,'ty/operations.html',{'e':k})

def eview(request,t):
	n = EmployeeDetails.objects.get(id=t)
	return render(request,'ty/eview.html',{'em':n})

def emup(request,p):
	m = EmployeeDetails.objects.get(id=p)
	if request.method == "POST":
		m.ename=request.POST['ename']
		m.eage=request.POST['eage']
		m.eusname=request.POST['eusname']
		m.eemail=request.POST['eemail']
		m.save()
		return redirect('/')
	return render(request,'ty/eup.html',{'et':m})

def emdl(request,f):
	b = EmployeeDetails.objects.get(id=f)
	if request.method == "POST":
		b.delete()
		return redirect('/')
	return render(request,'ty/edlt.html',{'edt':b})