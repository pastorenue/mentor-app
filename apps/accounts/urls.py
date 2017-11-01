from django.conf.urls import url
from .views import signup, activation_sent, activate

urlpatterns = [
	url(r'^signup$', signup, name="signup"),
	url(r'^account_activation_sent/$', activation_sent, name='activation_sent'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        activate, name='activate'),
]