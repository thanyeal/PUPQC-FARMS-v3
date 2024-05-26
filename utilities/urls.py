from django.urls import path

from utilities import views_schoolyear
from . import views

app_name = 'utilities'

urlpatterns = [
    path('', views.permissions, name='roles'),
    path('permissions/', views.permissions_edit, name='permissions'),
    path('types', views.req_type, name='types'),
    path('categories', views.req_cat, name='categories'),



    #--------------------------[ SCHOOL YEAR  MODULE URLS ]--------------------------#
    path('school-year/', views_schoolyear.main, name='school-year-main'),

]