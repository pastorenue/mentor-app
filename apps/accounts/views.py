from django.shortcuts import render, get_object_or_404
from mentor.forms import MentorProfessionalForm, MentorSignUpForm, BasicMentorForm
from expert.forms import ExpertProfessionalForm, ExpertSignUpForm, BasicExpertForm, AddressForm
from mentee.forms import MenteeSignUpForm, MenteeProfessionalForm, BasicMenteeForm
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .forms import CustomUserCreationForm
from django.core.urlresolvers import reverse
from django.db import transaction
from django.views.generic import ListView
from django.contrib.auth import login, authenticate, logout
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_text
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Quote
from random import randint
from mentee.models import MentorshipRequest, Mentee
from mentor.models import Mentor
from django.conf import settings
from django.contrib.sites.models import Site


def dashboard(request):
	template_name = 'accounts/dashboard.html'
	context = {}
	return render(request, template_name, context)

@transaction.atomic
def signup(request):
	template_name = 'accounts/signup.html'
	context = {}
	user_type = request.GET.get('user_type')

	if request.method == "POST":
		user_form = CustomUserCreationForm(request.POST)
		if user_form.is_valid():
			user = user_form.save(commit=False)
			user.save()
			if user_type == 'mentee':
				Mentee.objects.create(user=user)
			if user_type == 'mentor':
				Mentor.objects.create(user=user)
		try:
			notify(request, user)
		except Exception as e:
			messages.error(request, e)

		if user_type == 'mentee':
			return HttpResponseRedirect(reverse('mentee:edit'))
		else:
			return HttpResponseRedirect(reverse('mentor:edit'))
	else:
		user_form = CustomUserCreationForm()
		context = {'u_form': user_form}
		context['user_type'] = user_type
	return render(request, template_name, context)


def activation_sent(request):
	return render(request, 'accounts/account_activation_sent.html', {})


def activate(request, uidb64, token):
	try:
	    uid = force_text(urlsafe_base64_decode(uidb64))
	    user = User.objects.get(pk=uid)
	    if user is not None and account_activation_token.check_token(user, token):
	        user.is_active = True
	        user.save()
	        user = User.objects.get(pk=uid)
	        user.backend = 'django.contrib.auth.backends.ModelBackend'
	        login(request, user)
	        return reverse('mentee:mentee-list')
	except (TypeError, ValueError, OverflowError):
		messages.error(request, "Sorry! an error occured")
	return HttpResponseRedirect(reverse('mentee:mentee-list'))


def notify(request, user):
	user = user
	current_site = Site.objects.get_current().domain

	context_dict = {
        'name': '{0} {1}'.format(user.last_name, user.first_name),
        'user': user,
        'domain': current_site,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': account_activation_token.make_token(user),
    }
	txt_message = render_to_string('accounts/account_activation_email.txt', context_dict)
	html_message = render_to_string('accounts/account_activation_email.html', context_dict)
	subject, from_email, to = 'thebossoffice.com: Verification Required', 'no-reply@thebossoffice.com', user.username
	msg = EmailMultiAlternatives(subject, txt_message, from_email, [to])
	msg.attach_alternative(html_message, "text/html")
	try:
		msg.send()
		messages.info(request, 'Check your email.')
		user.is_active = True
		user.save()
		user.backend = 'django.contrib.auth.backends.ModelBackend'
		login(request, user)
		return redirect('accounts:activation_sent')
	except:#I activate the user if I can't send email and log.
	    user.is_active = True
	    user.save()
	    user.backend = 'django.contrib.auth.backends.ModelBackend'
	    login(request, user)

	    messages.success(request, "Welcome %s, your account is now active. You can now update your profile." % (user.first_name))
	    return reverse('mentee:mentee-list')

def alternative_notify(request):
	user.is_active = True
	user.save()
	login(request, user)
	messages.success(request, 'Your account is now active')

def landing_view(request):
	quote = None
	if Quote.objects.count() > 0:
		quote_pk = randint(1, Quote.objects.count())
		quote = get_object_or_404(Quote, pk=quote_pk)
	template_name = 'landing.html'
	context = {
		'quote': quote,
	}
	return render(request, template_name, context)


class MentorRequestListView(ListView):
	model = MentorshipRequest
	template_name = 'accounts/all_requests.html'
	context_object_name = "requests"
	paginated_by = settings.PAGE_SIZE

	def get_queryset(self):
		queryset = MentorshipRequest.objects.filter(to_user=self.request.user)
		print(queryset)
		return queryset


def mentorship_request(request):
	req = MentorshipRequest.objects.filter(to_user=request.user)

	context = {
		'requests': req
	}
	return 0
