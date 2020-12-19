from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('details', views.details, name='details'),
    path('success', views.success, name='success')
]