from django.shortcuts import render, get_object_or_404
from .models import Mentor
from django.views.generic import ListView, DetailView
from mentee.models import MentorshipRequest
from expert.models import Expert
from django.http import HttpResponseRedirect	
from django.core.urlresolvers import reverse
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db import transaction
# Create your views here.
class MentorListView(ListView):
	model = Mentor
	template_name = 'mentor/mentor_list.html'
	context_object_name = "mentors"

	def get_queryset(self):
		queryset = Mentor.objects.all()
		params = self.request.GET
		industry = params.get('industry')
		if hasattr(self.request.user, 'mentor'):
			queryset = queryset.exclude(user=self.request.user)
		if industry != 'all' and industry is not None:
			queryset = queryset.filter(industry=industry)
		return queryset

class MentorDetailView(DetailView):
	model = Mentor
	template_name = 'mentor/mentor_profile.html'
	slug_url_kwarg = 'slug'
	context_object_name = 'mentor'

	def get_context_data(self, **kwargs):
		context = super(MentorDetailView, self).get_context_data(**kwargs)
		self.mentor = context['mentor']
		context['waiting_connection'] = MentorshipRequest.objects.filter(to_user=self.mentor.user, status='O').exists()
		context['mentors_for_industry'] = Mentor.objects.exclude(user=self.mentor.user).filter(industry=self.mentor.industry)[:4]
		return context

@login_required
def edit_profile(request):
	linked_in = None
	instance = get_object_or_404(Mentor, user=request.user)
	if instance.linkedin_url:
		linked_in = instance.linkedin_url.split('/')[4]
	context = {}
	template_name = 'mentor/edit.html'
	if request.method == 'POST':
		form = MentorForm(request.POST, request.FILES, instance=instance)
		if form.is_valid():
			form = form.save(commit=False)
			form.user = request.user
			form.save()
			messages.success(request, "Your profile has been updated")
			return HttpResponseRedirect(reverse('mentor:mentor-profile', kwargs={'slug': instance.slug}))
	else:
		form = MentorForm(instance=instance)
		context['form'] = list(form)
		context['mentor'] = instance
		context['linkedin'] = linked_in

	return render(request, template_name, context)

@transaction.atomic
@login_required
def migrate_mentor(request):
	mentor = get_object_or_404(Mentor, user=request.user)
	mentor_fields = mentor.__dict__
	new_user = mentor.user
	field_exceptions = ['id','can_migrate','_state','date_modified', 'account_status']
	payload = {}
	for key,value in mentor_fields.items():
		if key in field_exceptions:
			continue
		else:
			payload[key] = value
	#import pdb; pdb.set_trace()
	try:
		expert = Expert.objects.create(**payload)
		mentor.delete()
		messages.success(request, 'Congratulations "%s"!!!. You have successfully been migrated to an Expert.' % (expert.name))
		return HttpResponseRedirect(reverse('expert:expert-profile', kwargs={'slug': expert.slug}))
	except:
		print(payload)
	return HttpResponseRedirect(reverse('mentor:mentor-list'))
