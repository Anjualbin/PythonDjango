from CMS.urls import path
from CRM import views

urlpatterns=[
    path("employee/add",views.employee_add),
    path("employee/<int:id>",views.employee_details),
    path("employee/change/<int:id>",views.employee_remove)
]