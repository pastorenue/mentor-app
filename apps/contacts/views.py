from django.shortcuts import render, redirect
from .models import Contact
from django.contrib import messages
# Create your views here.

def contact_us(request):
	if request.method == "POST":
		params = request.POST
		name = params.get('name', '')
		email = params.get('email', '')
		subject = params.get('subject', '')
		message = params.get('message', '')

		contact = Contact(name=name, email=email, subject=subject, message=message)
		contact.save()
		messages.success(request, "Thank you for reaching out to THEBOSSOFFICE.COM. \
			Your message will be treated with utmost importance")
	return redirect('home')