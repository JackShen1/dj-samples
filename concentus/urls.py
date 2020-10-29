from django.urls import path
from django.views.generic import TemplateView

app_name = 'concentus'
urlpatterns = [
    path('', TemplateView.as_view(template_name='concentus/index.html')),
]
