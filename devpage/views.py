from django.shortcuts import render
from . models import Project,contactForm,Contact
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.models import User
import threading

# Create your views here.
def index(request):
    pinnedProjects = Project.objects.filter(pin = True)[:3]
    return render(request, 'devpage/index.html',{'Projects':pinnedProjects})

def projects(request):
    Projects = Project.objects.filter(show = True)
    return render(request, 'devpage/projects.html',{'Projects': Projects})

def contact(request):
    success = ""
    if request.method == "POST":
        form = contactForm(request.POST)
        if form.is_valid():
            name = request.POST['name']
            email = request.POST['email']
            phone = request.POST['phone']
            concern = request.POST['desc']
            contactObj = Contact(name=name, email=email, phone=phone, desc=concern)
            contactObj.save()
            subject = f'Hi Harsha you got a message from {name}'
            message = f'phone: {phone}\nemail: {email}\nconcern: {concern}'
            email_from = settings.EMAIL_HOST_USER
            admin_user_emails = list(User.objects.filter(is_superuser=True).values_list('email', flat=True))
            mailThread = threading.Thread(target=send_mail, args=(subject, message, email_from, admin_user_emails,))
            mailThread.start()
            success = "Sent"
        else:
            success = "Failed"
    form = contactForm()
    return render(request, 'devpage/contact.html',{'form': form , 'success': success})

