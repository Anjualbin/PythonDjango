from django.shortcuts import render
from owner import forms

# Create your views here.

def home(request):
    return render(request,"index.html")

def additem(request):
    form=forms.MobileForm()
    context={"form":form}
    if request.method=="POST":
        form=forms.MobileForm(request.POST)
        if form.is_valid():
            name=form.cleaned_data["mobile_name"]
            model=form.cleaned_data["model"]
            price=form.cleaned_data["price"]
            print(name,model,price)
            context={}
            return render(request,"addnew.html")
    return render(request,"addnew.html",context)