from django.shortcuts import render 
from .models import Employee
from django.http import HttpResponse
def add_employee(request):
    if request.method == 'POST':
        name = request.POST['name']
        age = request.POST['age']
        department = request.POST['department']
        employee = Employee(name=name, age=age, department=department)
        employee.save()
        return HttpResponse(f"Employee {name} added successfully!")

    return render(request, 'add_employee.html')

def remove_employee(request):
    if request.method == 'POST':
        name = request.POST['name']
        try:
            employee = Employee.objects.get(name=name)
            employee.delete()
            return HttpResponse(f"Employee {name} removed successfully!")
        except Employee.DoesNotExist:
            return HttpResponse(f"Employee {name} not found!")

    return render(request, 'remove_employee.html')

def view_employee(request):
    if request.method == 'POST':
        name = request.POST['name']
        try:
            employee = Employee.objects.get(name=name)
            return render(request, 'view_employee.html', {'employee': employee})
        except Employee.DoesNotExist:
            return HttpResponse(f"Employee {name} not found!")

    return render(request, 'view_employee.html')

def list_employees(request):
    employees = Employee.objects.all()
    return render(request, 'list_employees.html', {'employees': employees})

