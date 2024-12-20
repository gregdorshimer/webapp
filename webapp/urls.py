from django.contrib import admin
from django.urls import include, path
from webapp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('resume/', views.resume, name='resume'),
    #path('dictionary/', include("dictionary.urls"), name='dictionary'),
    #path('wiki/', include("wiki.urls"), name='wiki'),
    path('sudoku/', include("sudoku.urls"), name='sudoku'),
    path('admin/', admin.site.urls)
]
