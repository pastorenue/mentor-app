from django.shortcuts import render, get_object_or_404
from .models import Mentee, MentorshipRequest
from django.views.generic import ListView, DetailView
from notifications.signals import notify
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from mentor.models import Mentor
from django.contrib import messages
from django.contrib.auth.models import User
from django.db import transaction
from .forms import *
from accounts.mailing import *
from expert.models import Address
from expert.forms import AddressForm

class MenteeListView(ListView):
	model = Mentee
	template_name = 'mentee/mentee_list.html'
	context_object_name = 'mentees'

	def get_queryset(self):
		queryset = Mentee.objects.all()
		params = self.request.GET
		industry = params.get('industry')
		if industry != 'all' and industry is not None:
			queryset = queryset.filter(industry=industry)
		if hasattr(self.request.user, 'mentee'):
			queryset = queryset.exclude(user=self.request.user)
		return queryset


class MenteeDetailView(DetailView):
	model = Mentee
	template_name = 'mentee/mentee_profile.html'
	slug_url_kwarg = 'slug'
	context_object_name = 'mentee'

	def get_context_data(self, **kwargs):
		context = super(MenteeDetailView, self).get_context_data(**kwargs)
		self.mentee = context['mentee']
		context['mentees_for_industry'] = Mentee.objects.filter(industry=self.mentee.industry).exclude(user=self.mentee.user)[:4]
		return context

@login_required
@transaction.atomic
def send_request(request, slug):
	mentor = Mentor.objects.get(slug=slug)
	new_notify = notify.send(request.user, 
							recipient=mentor.user, 
							verb="A mentor request has been sent",
							description="%s is demanding your services as a Mentor \
							in the area of %s" % (request.user.mentee, request.user.mentee.industry))
	if not MentorshipRequest.objects.filter(mentee=request.user, to_user=mentor.user,).exists():
		MentorshipRequest.objects.create(mentee=request.user, 
										to_user=mentor.user, 
										industry=mentor.industry)
		try:
			send_mentorship_mail(request, request.user, mentor.user)
		except:
			pass
	else:
		messages.info(request, "You have already sent a mentorship request to %s" % (mentor))
	return HttpResponseRedirect(reverse('mentee:mentee-profile', kwargs={'slug': request.user.mentee.slug}))

@login_required
@transaction.atomic
def accept(request, mentee_id, mentor_id):
	recipient = User.objects.get(pk=mentee_id)
	sender = User.objects.get(pk=mentor_id)
	m_request = MentorshipRequest.objects.get(mentee=recipient, to_user=sender)
	m_request.status = 'A'
	m_request.save()
	notify.send(request.user, 
				recipient=recipient, 
				verb="A mentor-request response has been sent.",
				description="Your mentorship request to %s has been accepted. \
				 You can communicate with Him now on %s" % (sender.mentor, sender))
	messages.success(request, "Thank you for your response. A notification will be sent to %s" % (recipient.mentee))
	return HttpResponseRedirect(reverse('mentee:mentee-list'))

@login_required
@transaction.atomic
def reject(request, mentee_id, mentor_id):
	mentee = User.objects.get(pk=mentee_id)
	mentor = User.objects.get(pk=mentor_id)
	m_request = MentorshipRequest.objects.get(mentee=mentee, to_user=mentor)
	m_request.status = 'D'
	m_request.save()
	notify.send(request.user, recipient=mentee, 
				verb="A mentor-request response has been sent.",
				description="Your mentorship request to %s was rejected \
				due to some reasons on the Mentor's part." % (mentor.mentor))
	messages.success(request, "Thank you for your response. A notification will be sent to %s" % (mentee.mentee))
	return HttpResponseRedirect(reverse('mentee:mentee-list'))


@login_required
def edit_profile(request):
	instance = get_object_or_404(Mentee, user=request.user)
	address = None
	try:
		address = get_object_or_404(Address, user=request.user)
	except:
		address = None
	context = {}
	template_name = 'mentee/edit.html'
	if request.method == 'POST':
		form = MenteeForm(request.POST, request.FILES, instance=instance)
		addr_form = AddressForm(request.POST, instance=address)
		if form.is_valid():
			form = form.save(commit=False)
			form.user = request.user
			if addr_form.is_valid():
				address = addr_form.save(commit=False)
				address.user = request.user
				address.save()
			form.address = address
			form.save()
			messages.success(request, "Your profile has been updated")
			return HttpResponseRedirect(reverse('mentee:mentee-profile', kwargs={'slug': instance.slug}))
	else:
		form = MenteeForm(instance=instance)
		addr_form = AddressForm(instance=address)
		context['form'] = list(form)
		context['addr_form'] = addr_form 
		context['mentee'] = instance

	return render(request, template_name, context)