from django.conf.urls import url
import django.contrib.auth.views

from .databaseTest import Forno
from django.views.generic import ListView

urlpatterns = [
    # Examples:
    url(r'^contact', ListView.as_view(model=Forno), name='forno_list'),
]
