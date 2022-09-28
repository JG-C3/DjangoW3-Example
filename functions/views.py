from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "index.html")

def image(request):
    return render(request, "image.html")

def lucky(request):
    return render(request, "lucky.html")

def birthday(request):
    return render(request, "birthday.html")

def table(request):
    return render(request, "table.html")
