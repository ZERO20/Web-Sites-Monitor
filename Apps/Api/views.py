#encoding:utf-8
from Apps.Monitor.models import Configuration, Monitoring
import requests
from rest_framework.response import Response
from rest_framework.views import APIView
import csv
import datetime
from django_datatables_view.base_datatable_view import BaseDatatableView
from django.db.models import Q

class CheckWebSiteStatus(APIView):

    def get(self,request):
        data = {}
        status = ''
        try:
            config = Configuration.objects.all()
            r = requests.get(config.first().url, timeout= config.first().frequency)
            data['error'] = False
            data['freq_val'] = config.first().frequency
            data['site'] = config.first().url

            if r.status_code == 200:
                data['avaliable']= True
                data['status'] = 'UP'
                status = 'UP'
            else:
                data['avaliable'] = False
                data['status'] = 'DOWN'
                status = 'DOWN'

            monitoring_reg = Monitoring.objects.create(status = status, url = config.first().url)
            writer = csv.writer(open('file-monitoring.csv','a'))
            writer.writerow([datetime.datetime.now().timestamp(), status, config.first().url], )
        except Exception as error:
            data['error'] = True
            data['msg'] = str(error)
        return Response(data)



class ApiMonitoringList(BaseDatatableView):
    model = Monitoring
    columns = ['id','url','create_date', 'status',]
    order_columns = ['id', 'url', 'create_date', 'status']
    max_display_length = 500

    def render_column(self, row, column):
        return super(ApiMonitoringList, self).render_column(row, column)

    def filter_queryset(self, qs):
        # use parameters passed in GET request to filter queryset
        start_date = self.request.GET.get(u'start_date',None)#extra parameters
        end_date = self.request.GET.get(u'end_date', None)#extra parameters
        status = self.request.GET.get(u'status', None)#extra parameters
        url = self.request.GET.get(u'url', None)#extra parameters
        search = self.request.GET.get(u'search[value]', None)

        if search:
            qs = qs.filter(Q(url__icontains=search)|Q(create_date__istartswith=search)|Q(status__istartswith=search))

        if start_date:
            qs = qs.filter(create_date__gte=end_date)

        if end_date:
            qs = qs.filter(create_date__lte=end_date)

        if status:
            qs = qs.filter(status__iexact=status)

        if url:
            qs = qs.filter(url__iexact=url)
        return qs
