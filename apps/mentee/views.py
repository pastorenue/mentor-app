from django.shortcuts import render
from .models import Mentee
from django.views.generic import ListView

# Create your views here.

class MenteeListView(ListView):
	model = Mentee
	template_name = 'mentee/mentee_list.html'
	context_object_name = 'mentees'
