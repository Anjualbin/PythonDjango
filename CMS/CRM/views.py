from django.shortcuts import render

# Create your views here.

def employee_add(request):
    return render(request,"emp_ad.html")

def employee_details(request,id):
    return render(request,"emp_view.html")

def employee_remove(request,id):
    return render(request,"emp_change.html")