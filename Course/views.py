from django.shortcuts import render

# Create your views here.

def View_Courses(request):
    return render(request, 'Site/index.html')