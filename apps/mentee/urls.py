from django.conf.urls import url
from .views import MenteeListView

urlpatterns = [
	url(r'^list$', MenteeListView.as_view(), name='mentee-list'),
]