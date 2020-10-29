from django.urls import path
from django.views.generic import TemplateView

app_name = 'infinity'
urlpatterns = [
    path('', TemplateView.as_view(template_name='infinity/index.html')),
]
