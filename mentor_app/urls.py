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
from accounts.views import dashboard

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

