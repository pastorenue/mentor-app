from django.conf.urls import url
from .views import MenteeListView, MenteeDetailView, send_request, accept, reject, edit_profile

urlpatterns = [
	url(r'^list$', MenteeListView.as_view(), name='mentee-list'),
	url(r'^edit$', edit_profile, name='edit'),
	url(r'^profile/(?P<slug>[\w-]+)$', MenteeDetailView.as_view(), name='mentee-profile'),
	url(r'^mentorship-request/(?P<slug>[\w-]+)$', send_request, name='send-request'),
	url(r'^mentorship-request/rejected/(?P<mentee_id>\d+)/(?P<mentor_id>\d+)$', reject, name='reject'),
	url(r'^mentorship-request/accepted/(?P<mentee_id>\d+)/(?P<mentor_id>\d+)$', accept, name='accept'),
	url(r'^list$', MenteeListView.as_view(), name='mentee-list'),
]