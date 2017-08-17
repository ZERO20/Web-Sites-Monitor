from django.conf.urls import url
from .views import CheckWebSiteStatus, ApiMonitoringList

urlpatterns = [
    url(r'^web/site/status/$', CheckWebSiteStatus.as_view(), name='check-web-site-status'),
    url(r'^monitoring/list/$', ApiMonitoringList.as_view(), name='api-monitoring-list'),
]
