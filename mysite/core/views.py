from django.shortcuts import render
from django.http import HttpResponse


def hello_world(request):
    return HttpResponse(content='hello world!')


def employees(request):
    return render(request, 'core/employees.html')


def employee_of_the_month(request):
    return render(request, 'core/employee_of_the_month.html')


def add_employee(request):
    return render(request, 'core/add_employee.html')
