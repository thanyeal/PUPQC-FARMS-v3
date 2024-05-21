from django.urls import path
from . import views

app_name = 'requirements'

urlpatterns = [

    path('bin', views.req_bin, name='bin'),
    path('categories', views.req_cat, name='categories'),
    path('setups', views.req_set, name='setups'),
    path('types', views.req_typ, name='types'),
]