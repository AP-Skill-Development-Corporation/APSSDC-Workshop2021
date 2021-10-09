from django.shortcuts import render,redirect
from Eapp.forms import UsReg,Crcty
from Eapp.models import CourseCategory

# Create your views here.
def home(request):
	return render(request,'html/home.html')

def about(request):
	return render(request,'html/about.html')

def contact(request):
	return render(request,'html/contact.html')

def register(request):
	if request.method == "POST":
		g = UsReg(request.POST)
		if g.is_valid():
			g.save()
			return redirect('/')
	g = UsReg()
	return render(request,'html/register.html',{'h':g})

def coursecty(request):
	m = CourseCategory.objects.all()
	if request.method == "POST":
		t = Crcty(request.POST)
		if t.is_valid():
			t.save()
			return redirect('/ccty')
	t = Crcty()
	return render(request,'html/crsectylist.html',{'g':t,'h':m})