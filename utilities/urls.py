from django.urls import path
from . import views

app_name = 'utilities'

urlpatterns = [
    path('', views.permissions, name='roles'),
    path('permissions/', views.permissions_edit, name='permissions'),
]