from django.shortcuts import render

# Create your views here.

# HomeScreenView
def home(request):
    return render(request, 'home.html')

