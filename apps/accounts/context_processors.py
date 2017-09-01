from mentor.models import Mentor
from expert.models import Industry
from forum.models import Channels, Post

def trending_data(request):
	get_profile = None
	if hasattr(request.user, 'mentor'):
		get_profile = request.user.mentor
	if hasattr(request.user, 'mentee'):
		get_profile = request.user.mentee
	if hasattr(request.user, 'expert'):
		get_profile = request.user.expert
	
	return {
		'industries': Industry.objects.all(),
		'latest_news': list(),
		'latest_mentors': list(),
		'newest_mentees': list(),
		'get_profile': get_profile,
		'channels': Channels.objects.all(),
	}