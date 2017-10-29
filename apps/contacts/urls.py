from django.conf.urls import url
from .views import *

urlpatterns = [
	url(r'^contact-us/$', contact_us, name="contact"),
]