#encoding: utf-8
from django.views.generic import TemplateView
from Apps.Monitor.models import Configuration

# Create your views here.

class MonitorDetailView(TemplateView):
    template_name = 'monitor_detail.html'

    def get_context_data(self, **kwargs):
        context = super(MonitorDetailView, self).get_context_data(**kwargs)
        context['configuration_act'] = Configuration.objects.all()
        return context


class MonitorListView(TemplateView):
    template_name = 'monitor_list.html'

    def get_context_data(self, **kwargs):
        context = super(MonitorListView, self).get_context_data(**kwargs)
        return context