from django.urls import path
from django.views.generic import TemplateView

app_name = 'heartverse'
urlpatterns = [
    path('', TemplateView.as_view(template_name='heartverse/index.html')),
]
