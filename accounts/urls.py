from django.urls import path
from accounts.views import authentication, accounts

app_name = 'accounts'

urlpatterns = [
    path('', accounts.accounts_module, name='users'),
    path('profile/', accounts.accounts_profile, name='profile'),
    path('login/', authentication.login_user, name='login'),

]