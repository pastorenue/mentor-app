from mentor.models import Mentor
from expert.models import Industry

def trending_data(request):
	return {
		'industries': Industry.objects.all(),
	}