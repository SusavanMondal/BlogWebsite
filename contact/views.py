from django.shortcuts import render
from .models import contact_list
from .models import contactform
# Create your views here.

def contactus(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        message=request.POST.get('message')

        contactformdata=contactform(Name=name, Email=email, Subject=subject, Message=message)
        contactformdata.save()

    contactdata=contact_list.objects.all()[0]
    context={
        "contactlist":contactdata,
    }
    return render(request, 'contact.html', context)
