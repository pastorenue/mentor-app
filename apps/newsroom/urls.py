from django.conf.urls import url
from .views import *

urlpatterns = [
	url(r"^$", NewsListView.as_view(), name="news-list"),
]