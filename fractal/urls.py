from django.urls import path
from django.views.generic import TemplateView

app_name = 'fractal'
urlpatterns = [
    path('', TemplateView.as_view(template_name='fractal/index.html')),
]
