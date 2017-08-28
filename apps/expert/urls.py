from django.conf.urls import url
from .views import ExpertListView, ExpertPublicDetailView

urlpatterns = [
	url(r'^list$', ExpertListView.as_view(), name='expert-list'),
	url(r'^detail/(?P<slug>[\w-]+)$', ExpertPublicDetailView.as_view(), name="expert-public-profile"),
]