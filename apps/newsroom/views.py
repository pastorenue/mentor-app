from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView, DetailView
from .models import *

class NewsListView(ListView):
	model = Entry
	template_name = 'newsroom/list.html'
	paginated_by = 2

	def get_context_data(self, **kwargs):
		context = super(NewsListView, self).get_context_data(**kwargs)
		entries = Entry.objects.all()
		paginator = Paginator(entries, self.paginated_by)

		page = self.request.GET.get('page')

		try:
			all_entries = paginator.page(page)
		except PageNotAnInteger:
			all_entries  = paginator.page(1)
		except EmptyPage:
			all_entries = paginator.page(paginator.num_pages)

		context['entries'] = all_entries
		context['recents'] = Entry.objects.get_recent()
		context['most_reads'] = Entry.objects.get_most_viewed()
		return context

class NewsDetailView(DetailView):
	model = Entry
	template_name = 'newsroom/news_detail.html'
	context_object_name = 'entry'
	slug_url_kwarg = 'slug'

