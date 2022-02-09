from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'devpage/index.html')

def projects(request):
    return render(request, 'devpage/projects.html')

def contact(request):
    return render(request, 'devpage/contact.html')