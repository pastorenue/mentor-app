from django.shortcuts import render
from .models import Mentor
from django.views.generic import ListView, DetailView
from mentee.models import MentorshipRequest

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
