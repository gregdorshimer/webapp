from django.urls import path

from . import views

app_name = 'wiki'
urlpatterns = [
    path('', views.index, name='index')
]
