from django.shortcuts import render
from Maths import forms
# Create your views here.

def view_home(request):
    return render(request,"index.html")


def add_nums(request):
    if request.method=="GET":
        form = forms.Calculation()
        context={"form":form}
        return render(request,"add_nums.html",context)
    elif request.method=="POST":
        form=forms.Calculation(request.POST)
        if form.is_valid():
            num1=form.cleaned_data["num1"]
            num2=form.cleaned_data["num2"]
            res=num1+num2
            context={"result":res}
            return render(request,"add_nums.html",context)
        return render(request, "add_nums.html")


def sub_nums(request):
    form = forms.Calculation()
    context = {"form": form}
    if request.method=="POST":
        form=forms.Calculation(request.POST)
        if form.is_valid():
            num1=form.cleaned_data["num1"]
            num2=form.cleaned_data["num2"]
            res=num1-num2
            context={"result":res}
            return render(request,"sub_nums.html",context)

    return render(request,"sub_nums.html",context)


def mul_nums(request):
    form = forms.Calculation()  # Creating an object for our form class Calcultion
    context = {"form": form}  # adding the form object to context dictionary to pass to django
    if request.method=="POST":
        form=forms.Calculation(request.POST)
        if form.is_valid():
            num1=form.cleaned_data["num1"]
            num2=form.cleaned_data["num2"]
            res=num1*num2
            context={"result":res}
            return render(request,"mul_nums.html",context)
    return render(request,"mul_nums.html",context)


def div_nums(request):
    form = forms.Calculation()
    context = {"form": form}
    if request.method=="POST":
        form=forms.Calculation(request.POST)
        if form.is_valid():
            num1=form.cleaned_data["num1"]
            num2=form.cleaned_data["num2"]
            res=num1/num2
            context={"result":res}
            return render(request,"div_nums.html",context)
    return render(request, "div_nums.html", context)
