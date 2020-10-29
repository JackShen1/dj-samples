from django.urls import path
from django.views.generic import TemplateView

app_name = 'spirals'
urlpatterns = [
    path('', TemplateView.as_view(template_name='spirals/index.html')),
]
