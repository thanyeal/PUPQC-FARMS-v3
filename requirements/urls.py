from django.urls import path
from requirements.views import requirement_bin, requirement_bin_setup


app_name = 'requirements'

urlpatterns = [
    # path('bin/setups', views.req_setup, name='setups'),
    # path('bin/assignees', views.req_assignees, name='assignees'),


    #--------------------------[ REQUIREMENT BIN MODULE URLS ]--------------------------#
    path('requirement-bin/', requirement_bin.main, name='requirement-bin'),
    path('requirement-bin/create/', requirement_bin.create, name='requirement-bin-create'),
    path('requirement-bin/edit/', requirement_bin.edit, name='requirement-bin-edit'),
    path('requirement-bin/soft-delete/', requirement_bin.soft_delete, name='requirement-bin-soft-delete'),
    path('requirement-bin/restore/', requirement_bin.restore, name='requirement-bin-restore'),
    path('requirement-bin/hard-delete/', requirement_bin.hard_delete, name='requirement-bin-hard-delete'),



    #--------------------------[ REQUIREMENT BIN SETUP MODULE URLS ]--------------------------#
    path('requirement-bin/setup/<uuid:requirement_bin_id>', requirement_bin_setup.main, name='requirement-bin-setup'),
    path('requirement-bin/setup/create/<uuid:requirement_bin_id>/', requirement_bin_setup.create, name='requirement-bin-setup-create'),
    path('requirement-bin/setup/soft-delete/', requirement_bin_setup.soft_delete, name='requirement-bin-setup-soft-delete'),
    path('requirement-bin/setup/restore/', requirement_bin_setup.restore, name='requirement-bin-setup-restore'),
    path('requirement-bin/setup/hard-delete/', requirement_bin_setup.hard_delete, name='requirement-bin-setup-hard-delete'),
] 