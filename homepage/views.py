from django.shortcuts import render


def index(request):
    """
    A view to return the homepage
    """
    return render(request, 'homepage/index.html')