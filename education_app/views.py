from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "index.html")

def about(request):
    return render(request, "user/about.html")

def contacts(request):
    return render(request, "user/contacts.html")

def typography(requests):
    return render(request, "user/typography.html")