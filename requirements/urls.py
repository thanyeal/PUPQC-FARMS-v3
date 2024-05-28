from django.urls import path
from requirements.views import requirement_bin


app_name = 'requirements'

urlpatterns = [
    # path('bin/setups', views.req_setup, name='setups'),
    # path('bin/assignees', views.req_assignees, name='assignees'),


    #--------------------------[ REQUIREMENT TYPE  MODULE URLS ]--------------------------#
    path('requirement-bin/', requirement_bin.main, name='requirement-bin'),
    path('requirement-bin/create/', requirement_bin.create, name='requirement-bin-create'),
    path('requirement-bin/edit/', requirement_bin.edit, name='requirement-bin-edit'),
    path('requirement-bin/soft-delete/', requirement_bin.soft_delete, name='requirement-bin-soft-delete'),
    path('requirement-bin/restore/', requirement_bin.restore, name='requirement-bin-restore'),
    path('requirement-bin/hard-delete/', requirement_bin.hard_delete, name='requirement-bin-hard=delete'),
] 