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
		if hasattr(self.request.user, 'mentor'):
			queryset = Mentor.objects.exclude(user=self.request.user)
		return queryset

class MentorPublicDetailView(DetailView):
	model = Mentor
	template_name = 'mentor/mentor_public_profile.html'
	slug_url_kwarg = 'slug'
	context_object_name = 'mentor'
