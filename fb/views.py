from django.shortcuts import render,HttpResponse
from fb.models import Contact
from django.contrib import messages
# Create your views here.

def home(request):
    return render(request, "index.html")

def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        password  = request.POST['name']
        sv = Contact(name=name, email=email, password=password)
        sv.save()
        messages.success(request, "Your message has been sent")
    return render(request, 'contact.html')