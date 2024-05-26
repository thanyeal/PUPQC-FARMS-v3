from django.shortcuts import render
import json


def main(request):
    state = 'active'
    serialized_state = json.dumps(state)
    context = {
        'requestz' : serialized_state , 
    }
    return render(request, 'school-year/main.html', context)



