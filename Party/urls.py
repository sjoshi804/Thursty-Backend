#-----------------------
# Purpose: Stores all urls associated with organizer side of the app
# Author: Siddharth Joshi
# Date Created: 04/18/18
#------------------------

from django.urls import path, re_path
from rest_framework.urlpatterns import format_suffix_patterns
from Party import views
 
urlpatterns = [
    re_path(r'^party/$', views.PartyList.as_view(), name='party-list'),
    re_path(r'^party/(?P<pk>[0-9]+)/$', views.PartyDetail.as_view(), name='party-detail'),
]