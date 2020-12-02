from django.urls import path
from django.conf.urls import url
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path('', views.HomeView.as_view()),
    url(r'^home/', TemplateView.as_view(template_name='home/main.html'), name='home'),
]

