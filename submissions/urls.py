from django.urls import path
from . import views

app_name = 'submissions'

urlpatterns = [

    path('', views.submissions_module, name='submissions_module'),
]