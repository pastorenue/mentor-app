from django.conf.urls import url
from .views import new_subscription

urlpatterns = [
    url(r'^subscribe/$', new_subscription, name="subscribe"),
]