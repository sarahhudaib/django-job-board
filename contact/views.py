from django.shortcuts import render, HttpResponseRedirect
from .models import Info
# from .form import InfoForm 
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.

def send_message(request):
    myinfo = Info.objects.first()

    if request.method == 'POST':
        subject = request.POST['subject']
        message = request.POST['message']
        email = request.POST['email']

        # print ('subject',subject)
        # print ('email',email)
        # print ('message',message)
        
        send_mail(
            subject,
            message,
            email,
            [settings.EMAIL_HOST_USER],
            # fail_silently=False,
        )
        return HttpResponseRedirect('/jobs/')
    else:
    #     myinfo = InfoForm
        
        return render(request,'contact/contact.html',{'myinfo':myinfo})