from django.shortcuts import render
from .models import *

def forum(request):
	return render(request, 'forum/discussion.html')

