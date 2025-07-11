from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_page, name='login'),
    path('username/', views.check_username, name='check_username'),
    path('email/', views.check_email, name='check_email'),
    path('password/', views.check_password, name='check_password'),
]
