from django.shortcuts import render

# Create your views here.

def jujutsu(request):
    return render(request,'templates/jujutsu.html')