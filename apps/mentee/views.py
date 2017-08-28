from django.shortcuts import render
from .models import Mentee
from django.views.generic import ListView, DetailView

# Create your views here.

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


class MenteePublicDetailView(DetailView):
	model = Mentee
	template_name = 'mentee/mentee_public_profile.html'
	slug_url_kwarg = 'slug'
	context_object_name = 'mentee'

	def get_context_data(self, **kwargs):
		context = super(MenteePublicDetailView, self).get_context_data(**kwargs)
		self.mentee = context['mentee']
		context['mentees_for_industry'] = Mentee.objects.filter(industry=self.mentee.industry).exclude(user=self.mentee.user)[:4]
		return context