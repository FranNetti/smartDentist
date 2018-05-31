from django.conf.urls import url
from django.contrib import admin

import smartDentistEP.views as views

urlpatterns = [
    url(r'^$', views.home, name="home"),
    url(r'^admin/', admin.site.urls),
    url(r'^ciao/', views.ciao, name="ciao"),
    url(r'^gpsData/', views.setGpsData, name="gpsData"),
]
