from django.urls import path
from utilities.views import requirement_category, requirement_type, school_year, school_year, semester


app_name = 'utilities'

urlpatterns = [
    path('', semester.permissions, name='roles'),
    path('permissions/', semester.permissions_edit, name='permissions'),
  

    #--------------------------[ SCHOOL YEAR  MODULE URLS ]--------------------------#
    path('school-year/', school_year.main, name='school-year-main'),
    path('school-year/create/', school_year.create, name='school-year-create'),
    path('school-year/edit/<uuid:pk>/', school_year.edit, name='school-year-edit'),
    path('school-year/soft-delete/<uuid:pk>/', school_year.soft_delete, name='school-year-soft-delete'),
    path('school-year/restore/', school_year.restore, name='school-year-restore'),
    path('school-year/hard-delete/<uuid:pk>/', school_year.hard_delete, name='school-year-hard=delete'),


    #--------------------------[ SEMESTER  MODULE URLS ]--------------------------#
    path('semester/', semester.main, name='semester-main'),
    path('semester/create/', semester.create, name='semester-create'),
    path('semester/edit/<uuid:pk>/', semester.edit, name='semester-edit'),
    path('semester/soft-delete/<uuid:pk>/', semester.soft_delete, name='semester-soft-delete'),
    path('semester/restore/', semester.restore, name='semester-restore'),
    path('semester/hard-delete/<uuid:pk>/', semester.hard_delete, name='semester-hard=delete'),




        #--------------------------[ REQUIREMENT CATEGORIES  MODULE URLS ]--------------------------#
    path('categories/', requirement_category.main, name='categories'),
    path('categories/create/', requirement_category.create, name='categories-create'),
    path('categories/edit/<uuid:pk>/', requirement_category.edit, name='categories-edit'),
    path('categories/soft-delete/<uuid:pk>/', requirement_category.soft_delete, name='categories-soft-delete'),
    path('categories/restore/', requirement_category.restore, name='categories-restore'),
    path('categories/hard-delete/<uuid:pk>/', requirement_category.hard_delete, name='categories-hard=delete'),


            #--------------------------[ REQUIREMENT TYPE  MODULE URLS ]--------------------------#
    path('categories/requirement-type/<uuid:category_id>/', requirement_type.main, name='requirement-type'),
    path('categories/requirement-type/create/', requirement_type.create, name='requirement-type-create'),
    path('categories/requirement-type/edit/', requirement_type.edit, name='requirement-type-edit'),
    path('categories/requirement-type/soft-delete/<uuid:category_id>/', requirement_type.soft_delete, name='requirement-type-soft-delete'),
    path('categories/requirement-type/restore/', requirement_type.restore, name='requirement-type-restore'),
    path('categories/requirement-type/hard-delete/<uuid:category_id>/', requirement_type.hard_delete, name='requirement-type-hard=delete'),




]