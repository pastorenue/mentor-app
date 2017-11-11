from django.conf.urls import url
from .views import MentorListView, MentorDetailView, edit_profile
from accounts.views import MentorRequestListView


urlpatterns = [
	url(r'^list$', MentorListView.as_view(), name="mentor-list"),
	url(r'^edit$', edit_profile, name='edit'),
	url(r'^detail/(?P<slug>[\w-]+)$', MentorDetailView.as_view(), name="mentor-profile"),
	url(r'^mentorship/requests$', MentorRequestListView.as_view(), name="mentorship-request"),

]