from django.shortcuts import render, get_object_or_404
from mentor.forms import MentorProfessionalForm, MentorSignUpForm, BasicMentorForm
from expert.forms import ExpertProfessionalForm, ExpertSignUpForm, BasicExpertForm, AddressForm
from mentee.forms import MenteeSignUpForm, MenteeProfessionalForm, BasicMenteeForm
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
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
from mentee.models import MentorshipRequest
from django.conf import settings


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
		user_form = basic_form = professional_form = None
		if user_type == 'mentor':
			user_form = MentorSignUpForm(request.POST)
			basic_form = BasicMentorForm(request.POST, request.FILES)
			professional_form = MentorProfessionalForm(request.POST, request.FILES)

		if user_type == 'mentee':
			user_form = MenteeSignUpForm(request.POST)
			basic_form = BasicMenteeForm(request.POST, request.FILES)
			professional_form = MenteeProfessionalForm(request.POST)
			addr_form = AddressForm(request.POST)
		if user_form.is_valid() and basic_form.is_valid() and professional_form.is_valid():
			user = user_form.save(commit=False)
			user.save()
			basic = basic_form.save(commit=False)
			if hasattr(basic, 'address_id'):
				if addr_form.is_valid:
					addr = addr_form.save(commit=False)
					addr.user = user
					addr.save()
					basic.address = addr
			basic.name = "%s, %s" % (user.first_name, user.last_name)
			basic.user = user
			basic.industry = professional_form.cleaned_data['industry']
			save_other_objects(basic, professional_form)
		try:
			notify(request, user)
		except:
			messages.error(request, "Sorry an Error was encountered. Try again later")

		return HttpResponseRedirect(reverse('mentee:mentee-list'))
	else:
		user_form = basic_form = professional_form = None
		if user_type == 'mentor':
			user_form = MentorSignUpForm()
			basic_form = BasicMentorForm()
			professional_form = MentorProfessionalForm()
			context = {'u_form': user_form, 'b_form': basic_form, 'p_form': professional_form}

		if user_type == 'mentee':
			user_form = MenteeSignUpForm()
			basic_form = BasicMenteeForm()
			professional_form = MenteeProfessionalForm()
			addr_form = AddressForm()
			context = {'a_form': addr_form, 'u_form': user_form, 'b_form': basic_form, 'p_form': professional_form}
		context['user_type'] = user_type
	return render(request, template_name, context)


def activation_sent(request):
	return render(request, 'accounts/account_activation_sent.html', {})


def activate(request, uidb64, token):
	import pdb; pdb.set_trace()
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
	current_site = get_current_site(request)
	context_dict = {
        'name': '{0} {1}'.format(user.last_name, user.first_name),
        'user': user,
        'domain': current_site.domain,
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
		messages.info(request, 'Check your email for a link to activate your account.')
		return redirect('accounts:activation_sent')
	except:#I activate the user if I can't send email and log.
	    user.is_active = True
	    user.save()
	    user.backend = 'django.contrib.auth.backends.ModelBackend'
	    login(request, user)

	    messages.success(request, 'Your account is now active')
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

def save_other_objects(base, other):
	basic = base
	if hasattr(basic, 'mode_details'):
		basic.mode_details = other.cleaned_data['mode_details']
	if hasattr(basic, 'mode_of_communication'):
		basic.mode_of_communication = other.cleaned_data['mode_of_communication']
	if hasattr(basic, 'name_of_business'):
		basic.name_of_business = other.cleaned_data['name_of_business']
	if hasattr(basic, 'level_of_education'):
		basic.level_of_education = other.cleaned_data['level_of_education']
	if hasattr(basic, 'time_with_mentor'):
		basic.time_with_mentor = other.cleaned_data['time_with_mentor']
	if hasattr(basic, 'year_of_commencement'):
		basic.year_of_commencement = other.cleaned_data['year_of_commencement']
	if hasattr(basic, 'type_to_handle'):
		basic.type_to_handle = other.cleaned_data['type_to_handle']
	if hasattr(basic, 'availability'):
		basic.availability = other.cleaned_data['availability']
	if hasattr(basic, 'linkedin_url'):
		basic.linkedin_url = other.cleaned_data['linkedin_url']
	if hasattr(basic, 'years_of_experience'):
		basic.years_of_experience = other.cleaned_data['years_of_experience']
	basic.save()


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
