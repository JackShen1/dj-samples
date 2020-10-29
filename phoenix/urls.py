from django.urls import path
from django.views.generic import TemplateView

app_name = 'phoenix'
urlpatterns = [
    path('', TemplateView.as_view(template_name='phoenix/index.html')),
]
