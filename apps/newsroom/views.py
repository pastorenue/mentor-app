from django.shortcuts import render
from django.views.generic import ListView
from .models import *

class NewsListView(ListView):
	model = Entry
	template_name = 'newsroom/list.html'
	context_object_name = 'entries'


