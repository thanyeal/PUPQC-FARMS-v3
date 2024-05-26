from django.urls import path
from utilities.views import requirement_category, requirement_type, school_year, school_year, semester


app_name = 'utilities'

urlpatterns = [
    path('', semester.permissions, name='roles'),
    path('permissions/', semester.permissions_edit, name='permissions'),
    path('types', requirement_type.req_type, name='types'),
    path('categories', requirement_category.req_cat, name='categories'),



    #--------------------------[ SCHOOL YEAR  MODULE URLS ]--------------------------#
    path('school-year/', school_year.main, name='school-year-main'),
    path('school-year/create/', school_year.create, name='school-year-create'),
    path('school-year/edit/<uuid:pk>/', school_year.edit, name='school-year-edit'),
    path('school-year/soft-delete/<uuid:pk>/', school_year.soft_delete, name='school-year-soft-delete'),
    path('school-year/restore/', school_year.restore, name='school-year-restore'),
    path('school-year/hard-delete/<uuid:pk>/', school_year.hard_delete, name='school-year-hard=delete'),


    #--------------------------[ SCHOOL YEAR  MODULE URLS ]--------------------------#
    path('semester/', semester.main, name='semester-main'),
    path('semester/create/', semester.create, name='semester-create'),
    path('semester/edit/<uuid:pk>/', semester.edit, name='semester-edit'),
    path('semester/soft-delete/<uuid:pk>/', semester.soft_delete, name='semester-soft-delete'),
    path('semester/restore/', semester.restore, name='semester-restore'),
    path('semester/hard-delete/<uuid:pk>/', semester.hard_delete, name='semester-hard=delete'),




]