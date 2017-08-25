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
		if hasattr(self.request.user, 'mentee'):
			queryset = queryset.exclude(user=self.request.user)
		return queryset

class MenteePublicDetailView(DetailView):
	model = Mentee
	template_name = 'mentee/mentee_public_profile.html'
	slug_url_kwarg = 'slug'
	context_object_name = 'mentee'
