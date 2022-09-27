from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index),
    path('image/', views.image),
    path('lucky/', views.lucky),
    path('birthday/', views.birthday),
    path('table/', views.table),
]