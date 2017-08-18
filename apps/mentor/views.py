from django.shortcuts import render
from .models import Mentor
from django.views.generic import ListView

# Create your views here.
class MentorListView(ListView):
	model = Mentor
	template_name = 'mentor/mentor_list.html'

	def get_queryset(self):
		queryset = super(MentorListView, self).get_queryset(**kwargs)
		params = self.request.GET
		industry = params.get('industry')
		if industry != 'all':
			queryset = Mentor.objects.filter(industry=industry)
		return queryset

	def get_context_data(self, **kwargs):
		context = super	(MentorListView, self).get_context_data(**kwargs)
		context['trending_mentors'] = Mentor.objects.trending_mentors()
		return context


def mentors(request):
	return render(request, 'mentor/mentor_list.html', {})