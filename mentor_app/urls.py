"""mentor_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView
from django.conf import settings as setting
from django.conf.urls.static import static
from django.core.urlresolvers import reverse
from accounts.views import dashboard
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^our-history$', TemplateView.as_view(template_name='_about.html'), name='about'),
    url(r'^home$', TemplateView.as_view(template_name='index.html'), name='home'),
    url(r'^$', TemplateView.as_view(template_name='landing.html'), name='landing'),
    url(r'^auth/dashboard$', dashboard, name='dashboard'),
    url(r'^accounts/', include('accounts.urls', namespace='accounts')),
    # url(r'^mentee/', include('mentee.urls', namespace='mentee')),
    # url(r'^mentor/', include('mentor.urls', namespace='mentor')),
    # url(r'^expert/', include('expert.urls', namespace='expert')),
]

urlpatterns+=static(setting.MEDIA_URL, document_root=setting.MEDIA_ROOT)

urlpatterns += [
    url(r'^auth/login/$', auth_views.LoginView.as_view(template_name='login.html'), name='user_login'),
    url(r'^auth/logout/$', auth_views.LogoutView.as_view(), name='logout'),
    url(r'^auth/password_change/$', auth_views.PasswordChangeView.as_view(success_url=reverse('home')), name='password_change'),
    url(r'^auth/password_change/done/$', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    url(r'^auth/password_reset/$', auth_views.PasswordResetView.as_view(success_url=reverse('home')), name='password_reset'),
    url(r'^auth/password_reset/done/$', auth_views.PasswordResetDoneView .as_view(), name='password_reset_done'),
    url(r'^auth/reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', auth_views.PasswordResetConfirmView.as_view(post_reset_login=True, success_url=reverse('home')), name='password_reset_confirm'),
    url(r'^auth/reset/done/$', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]