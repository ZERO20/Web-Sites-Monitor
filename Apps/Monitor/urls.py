from django.conf.urls import url
from Apps.Monitor.views import MonitorDetailView, MonitorListView

urlpatterns = [
    url(r'^$', MonitorDetailView.as_view(), name='monitor-detail'),
    url(r'^administration/$', MonitorListView.as_view(), name='monitor-list'),
]
