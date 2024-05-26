from django.urls import path
from . import views

app_name = 'requirements'

urlpatterns = [
    path('bin', views.req_bin, name='bin'),
    path('bin/setups', views.req_setup, name='setups'),
    path('bin/assignees', views.req_assignees, name='assignees'),
] 