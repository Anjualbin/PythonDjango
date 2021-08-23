from django.urls import path
from owner import views

urlpatterns=[
    path("",views.home,name="home"),
    path("addnew/",views.additem,name="additem")
]