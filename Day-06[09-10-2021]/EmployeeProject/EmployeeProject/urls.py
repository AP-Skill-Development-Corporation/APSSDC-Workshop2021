"""EmployeeProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Employee import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('demo/',views.sample),
    path('de/<str:name>/',views.dsname),
    path('fe/<str:name>/<int:age>/',views.fname),
    path('g/<str:fname>/<str:lname>/<int:sal>/',views.emp),
    path('gt/<str:empname>/<int:sal>/',views.empdetials),
    path('fy/<str:sname>/',views.dname),
    path('sty/<str:stname>/<int:year>/<str:branch>/',views.stname),
    path('reg/',views.regis),
    path('se/',views.index,name="ind"),
    path('about/',views.about,name="ab"),
    path('contact/',views.contact,name="cnt"),
    path('sam/',views.sample),
    path('re/',views.register,name="rg"),
    path('',views.operations,name="op"),
    path('emv/<int:t>/',views.eview,name="ev"),
    path('eup/<int:p>/',views.emup,name="ep"),
    path('ed/<int:f>/',views.emdl,name="edl"),
]
