from django.urls import path

from . import views

app_name = 'sudoku'
urlpatterns = [
    path('game/', views.GameAPIView.as_view(), name="game"),
    path('', views.index, name="index"),
]
