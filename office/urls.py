from django.urls import path
from . import views

urlpatterns = [
    path('', views.adminLogin, name='admin-login'),
    path('dashboard', views.Dashboard, name='dashboard')
]
