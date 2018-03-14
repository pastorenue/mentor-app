from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse


def send_mentorship_mail(request, sender, receiver):
	current_site = get_current_site(request)
	context_dict = {
		'sender': sender,
		'receiver': receiver,
		'domain': current_site.domain
	}

	try:
		txt_message = render_to_string('accounts/mentorship_request.txt', context_dict)
		html_message = render_to_string('accounts/mentorship_request.html', context_dict)
		subject, from_email, to = 'thebossoffice.com: mentorship Request', 'no-reply@thebossoffice.com', receiver.username
		msg = EmailMultiAlternatives(subject, txt_message, from_email, [to])
		msg.attach_alternative(html_message, "text/html")
		msg.send()

		messages.success(request, "Your mentorship request has been sent to %s" % (receiver.mentor))
	except Exception as e:
		messages.error(request, e)
	

def send_response_mail(request, sender, receiver):
	current_site = get_current_site(request)
	context_dict = {
		'sender': sender,
		'receiver': receiver,
		'domain': current_site.domain
	}

	import pdb; pdb.set_trace()

	txt_message = render_to_string('accounts/mentorship_request.txt', context_dict)
	html_message = render_to_string('accounts/mentorship_request.html', context_dict)
	subject, from_email, to = 'thebossoffice.com: Mentorship Response', 'no-reply@thebossoffice.com', user.username
	msg = EmailMultiAlternatives(subject, txt_message, from_email, [to])

