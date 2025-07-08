from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.person_create, name='person_create'),
    path('', views.person_list, name='person_list'),
]
