from django.conf.urls import url
from .views import MentorListView, MentorPublicDetailView


urlpatterns = [
	url(r'^list$', MentorListView.as_view(), name="mentor-list"),
	url(r'^detail/(?P<slug>[\w-]+)$', MentorPublicDetailView.as_view(), name="mentor-public-profile"),
]