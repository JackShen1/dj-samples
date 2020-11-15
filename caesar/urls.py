from django.urls import path
from django.views.generic import TemplateView

app_name = 'caesar'
urlpatterns = [
    path('', TemplateView.as_view(template_name='caesar/index.html')),
]
