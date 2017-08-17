from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.core.urlresolvers import reverse

urlpatterns = [
	
]
urlpatterns += [
    url(r'^auth/login$', auth_views.LoginView.as_view(template_name='login.html'), name='user_login'),
    url(r'^auth/logout$', auth_views.LogoutView.as_view(), name='logout'),
    url(r'^auth/password_change$', auth_views.PasswordChangeView.as_view(success_url=reverse('home')), name='password_change'),
    url(r'^auth/password_change/done$', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    url(r'^auth/password_reset$', auth_views.PasswordResetView.as_view(success_url=reverse('home')), name='password_reset'),
    url(r'^auth/password_reset/done$', auth_views.PasswordResetDoneView .as_view(), name='password_reset_done'),
    url(r'^auth/reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', auth_views.PasswordResetConfirmView.as_view(post_reset_login=True, success_url=reverse('home')), name='password_reset_confirm'),
    url(r'^auth/reset/done/$', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]