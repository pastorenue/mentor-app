from django.conf.urls import url
from .views import MentorListView, MentorDetailView


urlpatterns = [
	url(r'^list$', MentorListView.as_view(), name="mentor-list"),
	url(r'^detail/(?P<slug>[\w-]+)$', MentorDetailView.as_view(), name="mentor-profile"),
]