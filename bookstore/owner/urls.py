from django.urls import path
from owner import views

urlpatterns=[
    path("accounts/signup",views.signupview,name="signup"),
    path("accounts/signin",views.signinview,name="signin"),
    path("books/add",views.books_create,name="addbook"),
    path("books/",views.books_list,name="listbook"),
    path("",views.home,name="home")
# path("books/change/<int:id>",views.books_update,name="removebook"),
]