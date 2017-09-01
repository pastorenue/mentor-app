from django.shortcuts import render
from .models import *
from django.contrib import messages
from .models import Channels, Post, Comment
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.urlresolvers import reverse
from django.views.generic import ListView
from django.db import transaction

class PostListView(ListView):
	model = Post
	template_name = 'forum/discussion.html'
	context_object_name = 'posts'

	def get_queryset(self):
		queryset = Post.objects.all().order_by('-date_created')
		params = self.request.GET

		channel = params.get('channel')
		if channel != 'all' and channel is not None:
			queryset = queryset.filter(channels=channel)
		return queryset

	def get_context_data(self, **kwargs):
		channel_id = self.request.GET.get('channel')
		context = super(PostListView, self).get_context_data(**kwargs)
		if channel_id != 'all' and channel_id != None:
			context['current_channel'] = Channels.objects.get(pk=channel_id)
		else:
			context['current_channel'] = 'All Channels'
		return context

	@method_decorator(login_required)
	def dispatch(self, request, *args, **kwargs):
		return super(PostListView, self).dispatch(request, *args, **kwargs)

@login_required
@transaction.atomic
def new_post(request):
	if request.method == 'POST':
		params = request.POST
		body = params.get('comment')
		title = params.get('title')
		channel_id = params.get('channel')

		channel = Channels.objects.get(pk=channel_id)
		post = Post.objects.create(title=title, channels=channel, content=body, user=request.user)
		messages.success(request, "Post successfully created")
		return HttpResponseRedirect(reverse('forum:forum'))

@login_required
@transaction.atomic
def new_comment(request):
	if request.method == 'POST':
		params = request.POST
		body = params.get('reply')

		post_id = params.get('post_id')
		post = Post.objects.get(pk=post_id)
		Comment.objects.create(user=request.user, post=post, body=body)
		messages.success(request, "Comment successfully added")
		return HttpResponseRedirect(reverse('forum:forum'))
