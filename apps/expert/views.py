from django.shortcuts import render
from .models import Expert
from django.views.generic import ListView, DetailView

# Create your views here.
class ExpertListView(ListView):
	model = Expert
	template_name = 'expert/expert_list.html'
	context_object_name = 'experts'

	def get_queryset(self):
		queryset = Expert.objects.all()
		params = self.request.GET
		industry = params.get('industry')
		if industry != 'all' and industry is not None:
			queryset = queryset.filter(industry=industry)
		if hasattr(self.request.user, 'expert'):
			queryset = queryset.exclude(user=self.request.user)
		return queryset

class ExpertDetailView(DetailView):
	model = Expert
	template_name = 'expert/expert_profile.html'
	slug_url_kwarg = 'slug'
	context_object_name = 'expert'

	def get_context_data(self, **kwargs):
		context = super(ExpertDetailView, self).get_context_data(**kwargs)
		self.expert = context['expert']
		context['experts_for_industry'] = Expert.objects.filter(industry=self.expert.industry).exclude(user=self.expert.user)[:4]
		return context
