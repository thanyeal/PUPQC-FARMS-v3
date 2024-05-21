from django.shortcuts import render

# Create your views here.
def submissions_module(request):
    return render(request, 'submissions.html')
