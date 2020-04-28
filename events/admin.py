from django.contrib import admin
from events.models import Event, Task


class EventAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')

admin.site.register(Event, EventAdmin)


class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    exclude = ['percentage']

admin.site.register(Task, TaskAdmin)
