from django.shortcuts import render
from .models import Mentor
from django.views.generic import ListView, DetailView

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

class MentorPublicDetailView(DetailView):
	model = Mentor
	template_name = 'mentor/mentor_public_profile.html'
	slug_url_kwarg = 'slug'
	context_object_name = 'mentor'

	def get_context_data(self, **kwargs):
		context = super(MentorPublicDetailView, self).get_context_data(**kwargs)
		self.mentor = context['mentor']
		context['mentors_for_industry'] = Mentor.objects.exclude(user=self.mentor.user).filter(industry=self.mentor.industry)[:4]
		return context
