from django.shortcuts import render
from .models import Expert
from django.views.generic import ListView

# Create your views here.
class ExpertListView(ListView):
	model = Expert
	template_name = 'expert/expert_list.html'
	context_object_name = 'experts'

	def get_context_data(self, **kwargs):
		context = super(ExpertListView, self).get_context_data(**kwargs)

	def get_queryset(self):
		queryset = Expert.objects.all()
		params = self.request.GET
		industry = params.get('industry')
		if industry != 'all':
			queryset = queryset.filter(industry=industry)
		return queryset