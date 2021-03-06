from django.shortcuts import render, get_object_or_404
from .models import Expert
from django.views.generic import ListView, DetailView
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import *

from django.contrib import messages
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


@login_required
@user_passes_test(lambda u: u.expert)
def edit_profile(request):
	instance = get_object_or_404(Expert, user=request.user)
	context = {}
	template_name = 'expert/edit.html'
	if request.method == 'POST':
		form = ExpertForm(request.POST, request.FILES, instance=instance)
		if form.is_valid():
			form = form.save(commit=False)
			form.user = request.user
			form.save()
			messages.success(request, "Your profile has been updated")
			return HttpResponseRedirect(reverse('expert:expert-profile', kwargs={'slug': instance.slug}))
	else:
		form = ExpertForm(instance=instance)
		context['form'] = list(form)
		context['expert'] = instance

	return render(request, template_name, context)