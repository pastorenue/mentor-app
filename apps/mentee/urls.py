from django.conf.urls import url
from .views import MenteeListView, MenteeDetailView

urlpatterns = [
	url(r'^list$', MenteeListView.as_view(), name='mentee-list'),
	url(r'^profile/(?P<slug>[\w-]+)$', MenteeDetailView.as_view(), name='mentee-profile'),
]