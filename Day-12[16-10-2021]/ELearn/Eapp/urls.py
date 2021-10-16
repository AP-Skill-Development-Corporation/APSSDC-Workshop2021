from django.urls import path
from Eapp import views
from django.contrib.auth import views as ad

urlpatterns = [
	path('',views.home,name="hm"),
	path('abt/',views.about,name="ab"),
	path('cnt/',views.contact,name="ct"),
	path('reg/',views.register,name="rg"),
	path('ccty/',views.coursecty,name="cty"),
	path('crupd/<int:t>/',views.courseupd,name="crup"),
	path('crdlt/<int:y>/',views.coursedlt,name="crdl"),
	path('sbcrsl/',views.subcrlist,name="sbcrl"),
	path('sbcrvw/<int:w>/',views.subvw,name="sbvw"),
	path('sbcrup/<int:k>/',views.sbup,name="sbcrp"),
	path('sbcrdlt/<int:sd>/',views.sbdl,name="sbdlt"),
	path('login/',ad.LoginView.as_view(template_name='html/login.html'),name="lg"),
	path('logout/',ad.LogoutView.as_view(template_name='html/logout.html'),name="lgo"),
	path('dashb/',views.dashboard,name="dsh"),
	path('profle/',views.profile,name="pf"),
	path('pflup/',views.pfupd,name="pfu"),
	path('chgepwd/',views.changepwd,name="chgpw"),
	path('crlist/',views.stcrlist,name="stcrl"),
]