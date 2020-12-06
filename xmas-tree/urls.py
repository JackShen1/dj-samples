from django.urls import path
from django.views.generic import TemplateView

app_name = 'xmas-tree'
urlpatterns = [
    path('', TemplateView.as_view(template_name='xmas-tree/intro.html')),
    path('home/', TemplateView.as_view(template_name='xmas-tree/index.html'), name='xmas-home'),
    path('home/xmas-scene', TemplateView.as_view(template_name='xmas-tree/xmas-scene/index.html'), name='xmas-scene'),
    path('home/xmas-firework', TemplateView.as_view(template_name='xmas-tree/xmas-firework/index.html'), name='xmas-firework'),

]
