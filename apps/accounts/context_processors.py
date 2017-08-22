from mentor.models import Mentor
from expert.models import Industry

def trending_data(request):
	profile = None
	if hasattr(request.user, 'mentor'):
		profile = request.user.mentor
	if hasattr(request.user, 'mentee'):
		profile = request.user.mentee
	if hasattr(request.user, 'expert'):
		profile = request.user.expert
	return {
		'industries': Industry.objects.all(),
		'latest_news': list(),
		'latest_mentors': list(),
		'newest_mentees': list(),
		'profile': profile
	}