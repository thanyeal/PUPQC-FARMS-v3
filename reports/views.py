from django.shortcuts import render
import json
# Create your views here.
def reports_module(request):
    state = 'active'
    serialized_state = json.dumps(state)
    context = {
        'requestz' : serialized_state , 
    }
    return render(request, 'reports.html', context)