from django.conf.urls import url
from .views import mentors


urlpatterns = [
	url(r'^list$', mentors, name="mentor-list"),
]