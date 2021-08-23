from django.shortcuts import render,redirect
from owner import forms

# Create your views here.
def home(request):
    return render(request,"index.html")

def signupview(request):
    form=forms.RegistrationForm()
    context={"form":form}
    if request.method=="POST":
        form=forms.RegistrationForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            return redirect("signin")
    return render(request,"registration.html",context)

def signinview(request):
    form=forms.LoginForm()
    context={"form":form}
    if request.method=="POST":
        form=forms.LoginForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            return redirect("home")
    return render(request,"login.html",context)


def books_create(request):
    form= forms.BookForm()
    context={"form":form}
    if request.method=="POST":
        form=forms.BookForm(request.POST)
        if form.is_valid():
            bookname=form.cleaned_data["book_name"]
            author=form.cleaned_data["author"]
            price=form.cleaned_data["price"]
            copies=form.cleaned_data["copies"]
            print(bookname,author,price,copies)
            context={}
            return render(request,"books_add.html")
    return render(request,"books_add.html",context)

def books_list(request):
    return render(request,'books_list.html')

# def books_update(request,id):
#     return render(request,'books_change.html')