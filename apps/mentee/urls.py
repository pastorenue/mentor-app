from django.conf.urls import url
from .views import MenteeListView, MenteePublicDetailView

urlpatterns = [
	url(r'^list$', MenteeListView.as_view(), name='mentee-list'),
	url(r'^profile/(?P<slug>[\w-]+)$', MenteePublicDetailView.as_view(), name='mentee-public-profile'),
]