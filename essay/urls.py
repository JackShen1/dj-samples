from django.urls import path
from django.views.generic import TemplateView

app_name = 'essay'
urlpatterns = [
    path('', TemplateView.as_view(template_name='essay/index.html')),
]
