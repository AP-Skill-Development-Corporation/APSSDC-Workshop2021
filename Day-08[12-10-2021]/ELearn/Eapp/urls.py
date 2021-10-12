from django.urls import path
from Eapp import views

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
]