from django.conf.urls import url
from .views import ExpertListView

urlpatterns = [
	url(r'^list$', ExpertListView.as_view(), name='expert-list'),
]