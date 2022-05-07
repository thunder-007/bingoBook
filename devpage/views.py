from django.shortcuts import render
from . models import Project,contactForm,Contact
# Create your views here.
def index(request):
    pinnedProjects = Project.objects.filter(pin = True)[:3]
    return render(request, 'devpage/index.html',{'Projects':pinnedProjects})

def projects(request):
    Projects = Project.objects.filter(show = True)
    return render(request, 'devpage/projects.html',{'Projects': Projects})

def contact(request):
    if request.method == "POST":
        form = contactForm(request.POST)
        if form.is_valid():
            name = request.POST['name']
            email = request.POST['email']
            phone = request.POST['phone']
            concern = request.POST['desc']
            print(name, email, phone, concern)
            contactObj = Contact(name=name, email=email, phone=phone, desc=concern)
            contactObj.save()
            form = contactForm()
            return render(request, 'devpage/contact.html', {'form': form, 'submitted': True, 'try': True})
        else:
            form = contactForm()
            return render(request, 'devpage/contact.html', {'form': form, 'submitted': False, 'try': True})
    form = contactForm()
    return render(request, 'devpage/contact.html',{'form': form, 'submitted': False, 'Failed': False})