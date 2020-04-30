from django.contrib import admin
from employees.models import Employee


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'e_code', 'first_name', 'is_available', 'phone_main', 
    'hire_date', 'designation', 'added_by')
    list_display_links = ('id', 'e_code', 'first_name')
    list_editable = ('is_available',)
    exclude = ['point', 'added_by']

    def save_model(self, request, obj, form, change):
        obj.added_by = request.user
        super().save_model(request, obj, form, change)

admin.site.register(Employee, EmployeeAdmin)
