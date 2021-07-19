import django
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
import smtplib

# Create your views here.

# this is for Complaint Page
@login_required(login_url='login')
def comp(request):
    if request.method == 'POST':
        name = request.POST.get('full-name')
        email = request.POST.get('email')
        phone = request.POST.get('phone-number')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        data = {
            'name' : name,
            'email' : email,
            'phone' : phone,
            'subject' : subject,
            'message' : message
        }

        message = '''
            Name: {}
            Phone: {}
            New message: {}
            From: {}
        '''.format(data['name'], data['phone'], data['message'], data['email'])
        send_mail(data['subject'], message, '', ['mail@address.com']) # change the mail@address.com to ur desired mail address



    return render(request, 'complaint/complaint.html')