"""disambiguation_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('home.urls', namespace='home')),
    url(r'^wsd/',
        include(
            'wsd_proximate_collocations.wsd_proximate_collocations.urls',
            namespace="wsd"
        )),
    url(r'^sim_issues/',
        include(
            'sim_issues_app.sim_issues_app.urls',
            namespace="sim_issues"
        )),
    url(r'^text_assessment/',
        include(
            'text_assessment_app.text_assessment_app.urls',
            namespace='text_assessment'
        ))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
