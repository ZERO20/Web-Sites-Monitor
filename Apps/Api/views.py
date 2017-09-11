#encoding:utf-8
from Apps.Monitor.models import Configuration, Monitoring
import requests
from rest_framework.response import Response
from rest_framework.views import APIView
import csv
import datetime
from django_datatables_view.base_datatable_view import BaseDatatableView
from django.db.models import Q
from rest_framework import status

class CheckWebSiteStatus(APIView):

    def get(self,request):
        data = {}
        try:
            config = Configuration.objects.all()
            data['freq_val'] = config.first().frequency
            data['site'] = config.first().url
        except Exception as error:
            data['error'] = True
            data['msg'] = str(error)
            return Response(data, status= status.HTTP_500_INTERNAL_SERVER_ERROR)

        try:
            data['status'] = 'DOWN'
            r = requests.get(data['site'], timeout= data['freq_val'])
            if r.status_code == 200:
                data['status'] = 'UP'
        except Exception as e:
            pass

        #monitoring_reg = Monitoring.objects.create(status=data['status'], url=data['site'])
        writer = csv.writer(open('file-monitoring.csv','a'))
        writer.writerow([datetime.datetime.now().timestamp(), data['status'], data['site']],)
        return Response(data, status= status.HTTP_200_OK)


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
