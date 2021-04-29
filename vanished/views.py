from django.shortcuts import render


def home(request):
    return render(request, 'vanished/home.html')

def resources(request):
    return render(request, 'vanished/resources.html')

def about(request):
    return render(request, 'vanished/about.html')
