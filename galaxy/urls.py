from django.urls import path
from django.views.generic import TemplateView

app_name = 'galaxy'
urlpatterns = [
    path('', TemplateView.as_view(template_name='galaxy/index.html')),
]
