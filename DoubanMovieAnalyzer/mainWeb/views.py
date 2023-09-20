from django.shortcuts import render

def welcome(request):
    return render(request, 'mainWeb/welcome.html')

# Create your views here.
