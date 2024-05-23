from django.shortcuts import render
import json

def accounts_login(request):
    return render(request, 'auth/auth.html')

def accounts_module(request):
    state = 'active'
    serialized_state = json.dumps(state)
    context = {
        'requestz' : serialized_state , 
    }
    return render(request, 'accounts.html', context)
