from django.urls import path
from django.views.generic import TemplateView

app_name = 'constellation'
urlpatterns = [
    path('', TemplateView.as_view(template_name='constellation/index.html')),
]
