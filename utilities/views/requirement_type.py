from django.http import JsonResponse
from django.shortcuts import render
import json
from django.contrib import messages

def req_type(request):
    state = 'active'
    serialized_state = json.dumps(state)
    context = {
        'requestz' : serialized_state , 
    }
    return render(request, 'req_typ.html', context)
