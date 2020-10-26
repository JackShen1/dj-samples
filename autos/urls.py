from django.urls import path
from . import views
from django.views.generic import TemplateView

# We basically have a main table, which is our autos table, and our lookup table, which is our makes table. Then we have
# three things, there is the main list view, which is list all the autos. There is the main Make list view, which is
# list all the makes. Then we can make a new one which doesn't have a primary key, because part of the ideas that create
# is making a new thing, which is going to generate a primary key. Then we're going to have update and a delete.
# So we have a read, create, update, delete. So it's not exactly cred, but you see all four of these things. So we've
# got views, and we name these views so that we can reference them in our views themselves and in our template so we can
# make links in between them. So these are pretty straightforward and not all that different.

# https://docs.djangoproject.com/en/3.0/topics/http/urls/
app_name='autos'
urlpatterns = [
    path('', views.MainView.as_view(), name='all'),
    path('main/create/', views.AutoCreate.as_view(), name='auto_create'),
    path('main/<int:pk>/update/', views.AutoUpdate.as_view(), name='auto_update'),
    path('main/<int:pk>/delete/', views.AutoDelete.as_view(), name='auto_delete'),
    path('lookup/', views.MakeView.as_view(), name='make_list'),
    path('lookup/create/', views.MakeCreate.as_view(), name='make_create'),
    path('lookup/<int:pk>/update/', views.MakeUpdate.as_view(), name='make_update'),
    path('lookup/<int:pk>/delete/', views.MakeDelete.as_view(), name='make_delete'),
]

# Note that make_ and auto_ give us uniqueness within this application

