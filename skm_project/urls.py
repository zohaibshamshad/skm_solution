from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from pages import views
from events import views as task_views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('home/', include('pages.urls')),
    path('employees/', include('employees.urls')),
    path('accounts/', include('accounts.urls')),
    path('events/', include('events.urls')),
    path('<int:task_id>', task_views.task, name='task'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
