from django.contrib.auth.decorators import login_required
from django.urls import path
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path('', views.HomeView.as_view()),
    path('intro/', TemplateView.as_view(template_name='home/intro.html'), name='intro'),
    path('home/', TemplateView.as_view(template_name='home/main.html'), name='home_page'),
]

