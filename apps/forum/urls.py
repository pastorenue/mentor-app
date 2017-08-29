from django.conf.urls import url
from .views import forum

urlpatterns = [
	url(r'^$', forum, name="forum"),
]