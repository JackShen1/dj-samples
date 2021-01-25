from django.contrib.auth.decorators import login_required
from django.urls import path
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path('', views.HomeView.as_view()),
    path('intro/', TemplateView.as_view(template_name='home/intro.html'), name='intro'),
    path('home/', TemplateView.as_view(template_name='home/main.html'), name='home_page'),
    path('home/concentus', TemplateView.as_view(template_name='concentus/index.html'), name='concentus'),
    path('home/constellation', TemplateView.as_view(template_name='constellation/index.html'), name='constellation'),
    path('home/expressionism', TemplateView.as_view(template_name='expressionism/index.html'), name='expressionism'),
    path('home/expressionism2', TemplateView.as_view(template_name='expressionism2/index.html'), name='expressionism2'),
    path('home/fractal', TemplateView.as_view(template_name='fractal/index.html'), name='fractal'),
    path('home/galaxy', TemplateView.as_view(template_name='galaxy/index.html'), name='galaxy'),
    path('home/heartverse', TemplateView.as_view(template_name='heartverse/index.html'), name='heartverse'),
    path('home/infinity', TemplateView.as_view(template_name='infinity/index.html'), name='infinity'),
    path('home/neon', TemplateView.as_view(template_name='neon/index.html'), name='neon'),
    path('home/phoenix', TemplateView.as_view(template_name='phoenix/index.html'), name='phoenix'),
    path('home/spirals', TemplateView.as_view(template_name='spirals/index.html'), name='spirals'),
    path('home/whirlpool', TemplateView.as_view(template_name='whirlpool/index.html'), name='whirlpool'),
]

