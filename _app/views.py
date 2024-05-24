from django.shortcuts import render

def accounts_login(request):
    return render(request, 'auth/auth.html')
