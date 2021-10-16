from django.shortcuts import render,redirect
from Eapp.forms import UsReg,Crcty,SbCrl,Pfupdf,ChgPwd
from Eapp.models import CourseCategory,SubCourse,User
from django.contrib import messages
from django.contrib.auth.decorators import login_required

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
			return redirect('/login')
	g = UsReg()
	return render(request,'html/register.html',{'h':g})

@login_required
def coursecty(request):
	m = CourseCategory.objects.filter(usd_id=request.user.id)
	if request.method == "POST":
		t = Crcty(request.POST,request.FILES)
		if t.is_valid():
			d = t.save(commit=False)
			d.usd_id = request.user.id
			# print(g.ctitle,g.cimg,g.usd_id,request.user.id)
			d.save()
			return redirect('/ccty')
	t = Crcty()
	return render(request,'html/crsectylist.html',{'g':t,'h':m})

@login_required
def courseupd(request,t):
	k = CourseCategory.objects.get(id=t)
	if request.method == "POST":
		j = Crcty(request.POST,instance=k)
		if j.is_valid():
			j.save()
			return redirect('/ccty')
	j = Crcty(instance=k)
	return render(request,'html/crsupd.html',{'p':j})

@login_required
def coursedlt(request,y):
	r = CourseCategory.objects.get(id=y)
	if request.method == "POST":
		r.delete()
		return redirect('/ccty')
	return render(request,'html/crdlt.html',{'n':r})

@login_required
def subcrlist(request):
	sd,b = {},0
	m = SubCourse.objects.all()
	# p = CourseCategory.objects.all()
	nj = list(CourseCategory.objects.filter(usd_id=request.user.id))
	print(nj)
	for i in m:
		for j in nj:
			if i.crs_id == j.id:
				sd[b] = j.ctitle,i.sbtitle,i.price,i.id
				b+=1
	if request.method == "POST":
		y = SbCrl(request.POST)
		if y.is_valid():
			z = y.save(commit=False)
			z.save()
			messages.success(request,"SubCourse Added Successfully")
			return redirect('/sbcrsl')
	y = SbCrl()
	return render(request,'html/subcrlist.html',{'r':y,'d':sd.values(),'cv':nj})

@login_required
def subvw(request,w):
	k = SubCourse.objects.get(id=w)
	print(k.crs_id)
	nj = CourseCategory.objects.get(id=k.crs_id)
	return render(request,'html/subvew.html',{'g':k,'b':nj})

@login_required
def sbup(request,k):
	g = SubCourse.objects.get(id=k)
	if request.method == "POST":
		f = SbCrl(request.POST,instance=g)
		if f.is_valid():
			f.save()
			messages.info(request,"SubCourse Added Successfully")
			return redirect('/sbcrsl')
	f = SbCrl(instance=g)
	return render(request,'html/sbup.html',{'a':f})

@login_required
def sbdl(request,sd):
	v = SubCourse.objects.get(id=sd)
	if request.method == "POST":
		v.delete()
		messages.warning(request,"SubCourse Added Successfully")
		return redirect('/sbcrsl')
	return render(request,'html/sdt.html',{'c':v})

@login_required
def dashboard(request):
	return render(request,'html/dashboard.html')

@login_required
def profile(request):
	return render(request,'html/profile.html')

@login_required
def pfupd(request):
	j = User.objects.get(id=request.user.id)
	if request.method == "POST":
		g = Pfupdf(request.POST,request.FILES,instance=j)
		if g.is_valid():
			g.save()
			return redirect('/profle')
	g = Pfupdf(instance=j)
	return render(request,'html/pfupd.html',{'h':g})

@login_required
def changepwd(request):
	if request.method == "POST":
		b = ChgPwd(user=request.user,data=request.POST)
		if b.is_valid():
			b.save()
			return redirect('/login')
	b = ChgPwd(user=request.user)
	return render(request,'html/changepaswd.html',{'c':b})

@login_required
def stcrlist(request):
	gh,y = {},0
	k = SubCourse.objects.all()
	m = CourseCategory.objects.all()
	for i in m:
		for j in k:
			if i.id == j.crs_id:
				gh[y] = i.ctitle,i.cimg,j.sbtitle,j.price
				y+=1
	return render(request,'html/stcolist.html',{'x':gh.values()})