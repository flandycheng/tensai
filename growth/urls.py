"""tensai URL Configuration
"""
from django.conf.urls import url, include
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^charge/', include('growth.charge.urls')),
    url(r'^experience/', include('growth.experience.urls')),
    url(r'^admin/', admin.site.urls),
]
