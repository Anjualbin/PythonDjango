from django.urls import path
from Maths import views

urlpatterns=[
    path("addnum",views.add_nums,name="addnums"),
    path("subnum",views.sub_nums,name="subnums"),
    path("mulnum",views.mul_nums,name="mulnums"),
    path("divnum",views.div_nums,name="divnums"),
    path("",views.view_home,name="home")
]