from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('',views.index,name='index'),
    path('projects',views.projects,name='projects'),
    path('contact',views.contact,name='contact'),
    path('react',TemplateView.as_view(template_name='index.html'))
]
