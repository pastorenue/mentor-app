from mentor.models import Mentor
from expert.models import Industry, Expert
from forum.models import Channels, Post
from mentee.models import MentorshipRequest

def trending_data(request):
	get_profile = None
	is_connected = False
	if hasattr(request.user, 'mentor'):
		get_profile = request.user.mentor
	if hasattr(request.user, 'mentee'):
		get_profile = request.user.mentee
	if hasattr(request.user, 'expert'):
		get_profile = request.user.expert
	if not request.user.is_anonymous():
		is_connected = MentorshipRequest.objects.filter(mentee=request.user, status='A').exists()
	
	return {
		'industries': Industry.objects.all(),
		'latest_news': list(),
		'trending_experts': Expert.objects.all().order_by('-date_created')[:3],
		'latest_mentors': list(),
		'newest_mentees': list(),
		'get_profile': get_profile,
		'channels': Channels.objects.all(),
		'is_connected': is_connected
	}