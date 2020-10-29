from django.urls import path
from django.views.generic import TemplateView

app_name = 'expressionism2'
urlpatterns = [
    path('', TemplateView.as_view(template_name='expressionism2/index.html')),
]
