from django.shortcuts import render

# Create your views here.
def monitoring_module(request):
    return render(request, 'monitoring.html')
