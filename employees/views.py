from django.shortcuts import render, redirect, get_object_or_404
from employees.models import Employee

def index(request):
    return render(request, 'employees/index.html')
    
def employee(request, employee_id):
    employee = get_object_or_404(Employee, pk=employee_id)
    cnic = employee.cnic
    employee.cnic = '-'.join((cnic[:5], cnic[5:12], cnic[12]))
    context = {
        'employee' : employee,
    }
    return render(request, 'employees/employee.html', context)

def employees(request):
    employees = Employee.objects.order_by('hire_date')
    context = {
        'employees' : employees
    }
    return render(request, 'employees/employees.html', context)
