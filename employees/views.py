from django.shortcuts import render, redirect, get_object_or_404
from employees.models import Employee
from django.views.generic import ListView, DetailView
from rest_framework import viewsets
from employees.serializers import EmployeeSerializer

class EmployeeView(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class EmployeesListView(ListView):
    model = Employee
    context_object_name = 'employees'
    template_name = 'employees/employees.html'
    ordering = '-hire_date'
    paginate_by = 10

class EmployeesDetailView(DetailView):
    model = Employee
    context_object_name = 'employee'
    template_name = 'employees/employee.html'

    def get_object(self):
        employee = get_object_or_404(Employee, pk=self.kwargs.get('pk'))
        cnic = employee.cnic
        employee.cnic = '-'.join((cnic[:5], cnic[5:12], cnic[12]))
        return employee


def index(request):
    return render(request, 'employees/index.html')

# def employee(request, employee_id):
#     employee = get_object_or_404(Employee, pk=employee_id)
#     cnic = employee.cnic
#     employee.cnic = '-'.join((cnic[:5], cnic[5:12], cnic[12]))
#     context = {
#         'employee' : employee,
#     }
#     return render(request, 'employees/employee.html', context)

# def employees(request):
#     employees = Employee.objects.order_by('hire_date')
#     context = {
#         'employees' : employees
#     }
#     return render(request, 'employees/employees.html', context)
