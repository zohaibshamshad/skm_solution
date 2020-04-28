from django.shortcuts import render, get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from events.models import Event, Task

def events(request):
    events = Event.objects.order_by('-event_date')
    page = request.GET.get('page')
    paginator = Paginator(events, 6)
    paged_events = paginator.get_page(page)
    context = {
        'events' : paged_events,
    }
    return render(request, 'events/events.html', context)
    
def event(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    tasks = Task.objects.order_by('-task_date')
    context = {
        'event' : event,
        'tasks' : tasks,
    }
    return render(request, 'events/event.html', context)

def tasks(request):
    tasks = Task.objects.order_by('-task_date')
    context = {
        'tasks' : tasks,
    }
    return render(request, 'events/tasks.html', context)

def task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    context = {
        'task' : task,
    }
    return render(request, 'events/task.html', context)
