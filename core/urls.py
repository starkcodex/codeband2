
from django.urls import path, include
from .import views
from django.conf.urls.static import static 
from django.conf import settings


urlpatterns = [
    path('', views.homeview, name='home-page'),
    path('project/', views.project_listview, name='project-page')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
