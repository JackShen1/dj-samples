from django.urls import path
from django.views.generic import TemplateView

app_name = 'whirlpool'
urlpatterns = [
    path('', TemplateView.as_view(template_name='whirlpool/index.html')),
]
