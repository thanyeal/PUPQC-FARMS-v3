from django.urls import path
from . import views

app_name = 'submissions'

urlpatterns = [

    path('', views.submissions_module, name='submission'),
    path('list/', views.submissions_list, name='listreqs'),
]