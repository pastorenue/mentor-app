from django.shortcuts import render

# Create your views here.

def mentors(request):
	return render(request, 'mentor/mentor_list.html', {})