from django.conf.urls import url
from .views import ExpertListView, ExpertDetailView, edit_profile

urlpatterns = [
	url(r'^list$', ExpertListView.as_view(), name='expert-list'),
	url(r'^edit$', edit_profile, name='edit'),
	url(r'^detail/(?P<slug>[\w-]+)$', ExpertDetailView.as_view(), name="expert-profile"),
]