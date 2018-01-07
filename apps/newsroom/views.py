from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView, DetailView
from .models import *
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.contrib import messages
from django.conf import settings

class NewsListView(ListView):
	model = Entry
	template_name = 'newsroom/list.html'
	paginated_by = settings.PAGE_SIZE

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

		context['entries'] = Entry.objects.get_others()
		context['recents'] = Entry.objects.get_recent()
		context['most_reads'] = Entry.objects.get_most_viewed()

		return context

class NewsDetailView(DetailView):
	model = Entry
	template_name = 'newsroom/news_detail.html'
	context_object_name = 'entry'
	slug_url_kwarg = 'slug'

	def dispatch(self, request, *args, **kwargs):
		# entry = self.
		# entry.views+=1
		# entry.save()
		return super(NewsDetailView, self).dispatch(request, *args, **kwargs)

def news_detail(request, slug):
	template_name = 'newsroom/news_detail.html'
	entry = Entry.objects.get(slug=slug)
	entry.views+=1
	entry.save()
	return render(request, template_name, {'entry':entry})

@login_required
@transaction.atomic
def new_comment(request):
	if request.method == 'POST':
		params = request.POST
		body = params.get('body')

		entry_id = params.get('entry_id')
		entry = Entry.objects.get(pk=entry_id)
		try:
			Comment.objects.create(user=request.user, entry=entry, body=body)
			messages.success(request, "Comment successfully added")
			return HttpResponseRedirect(reverse('newsroom:news-detail', kwargs={'slug':entry.slug}))
		except: 
			messages.error(request, "Please register to post a comment")
			return HttpResponseRedirect(reverse('accounts:signup'))
