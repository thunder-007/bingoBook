from django.db import models
from cloudinary.models import CloudinaryField
from captcha.fields import CaptchaField
from django import forms
class Tag(models.Model):
    color = models.CharField(max_length=20)
    text = models.CharField(max_length=20)
    def __str__(self):
        return self.text
# Create your models here.
class Project(models.Model):
    projectTemplate = CloudinaryField('image')
    projectTitle = models.TextField(default="Title ")
    desc = models.TextField(default="not mentioned")
    projectLink = models.URLField(max_length=200, default="not mentioned")
    created_at = models.DateTimeField(auto_now_add=True)
    tags = models.ForeignKey(Tag,on_delete=models.PROTECT)
    show = models.BooleanField()
    pin = models.BooleanField()
    def __str__(self):
        return f'{self.projectTitle} - {self.desc[:15]} ..'


class contactForm(forms.Form):
    captcha = CaptchaField()


class Contact(models.Model):
    name = models.CharField(max_length=30, default="not mentioned")
    email = models.EmailField(default="not mentioned")
    phone = models.CharField(max_length=15, default="not mentioned")
    desc = models.TextField(default="not mentioned")

    def __str__(self):
        return f'{self.name} - {self.desc[:15]} ..'
