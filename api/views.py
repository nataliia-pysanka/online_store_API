from rest_framework import viewsets, views
from .serializer import ProductSerializer, OrderSerializer
from .models import Product, Order
from rest_framework import filters
from datetime import datetime
from rest_framework.response import Response
from django.db.models import Sum, Count
from re import search as re_search, IGNORECASE


def get_date(str_date: str):
    """
    Parses the inputted string and returns datetime object
    """
    date_formats = ['%Y-%m', '%Y/%m', '%Y%m',
                    '%Y-%b', '%Y/%b', '%Y%b',
                    '%Y-%B', '%Y/%B', '%Y%B',
                    '%Y-%m-%d', '%Y/%m/%d', '%Y%m%d',
                    '%Y-%b-%d', '%Y/%b/%d', '%Y%b%d',
                    '%Y-%B-%d', '%Y/%B/%d', '%Y%B%d']

    if str_date is None:
        return None

    for d_f in date_formats:
        try:
            date_ = datetime.strptime(str_date, d_f)
            return date_
        except ValueError:
            continue
    return None


def get_next_month(date_: datetime):
    """
    Returns datetime object with increased on 1 month value
    """
    year, month = date_.year, date_.month
    month += 1
    if month > 12:
        month = 1
        year = date_.year + 1
    date_ = date_.replace(year=year, month=month)
    return date_


class ProductViewSet(viewsets.ModelViewSet):
    """
    View for list of all Product
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class OrderViewSet(viewsets.ModelViewSet):
    """
    View for list of all Orders
    """
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['date']


class StatsViewSet(views.APIView):
    """
    View for list of statistic data
    """

    def query_sum(self, obj: Order):
        """
        Returns aggregation function Sum for products of Order instance for
        field 'price'
        """
        month_value = obj.products.aggregate(Sum('price'))
        month_value = month_value.get('price__sum')
        month_value = 0 if month_value is None else month_value
        return month_value
    
    def query_count(self, obj: Order):
        """
        Returns aggregation function Count for products of Order instance for
        field 'title'
        """
        month_count = obj.products.aggregate(Count('title'))
        month_count = month_count.get('title__count')
        month_count = 0 if month_count is None else month_count
        return month_count

    def counter(self, agg_func, queryset: [Order]):
        """
        Returns dict with results of aggregation function calculations for
        every month in list
        """
        stat_dict = {}
        for obj in queryset:
            value = agg_func(obj)
            date = obj.date.strftime('%Y %b')
            if stat_dict.get(date):
                old_value = stat_dict.get(date)
                stat_dict.update({date: old_value + value})
            else:
                stat_dict.update({date: value})
        return stat_dict

    def get(self, request):
        """
        Returns a list of all the orders for the specific time term
        """
        queryset = Order.objects.all()
        date_start = self.request.query_params.get('date_start', None)
        date_end = self.request.query_params.get('date_end', None)
        metric = self.request.query_params.get('metric', 'price')

        date_start = get_date(date_start)

        if date_start is None:
            date_start = datetime(year=1900, month=1, day=1)

        date_end = get_date(date_end)

        if date_end is None:
            date_end = datetime.now()

        date_end = get_next_month(date_end)

        if re_search(r'price', metric, IGNORECASE):
            metric = 'price'
        elif re_search(r'count', metric):
            metric = 'count'
        else:
            metric = 'price'

        stat = []
        queryset = queryset.filter(
            date__range=[date_start, date_end]).order_by('date')
        stat_dict = {}
        match metric:
            case 'price':
                stat_dict = self.counter(self.query_sum, queryset)
            case 'count':
                stat_dict = self.counter(self.query_count, queryset)

        for month, value in stat_dict.items():
            stat.append({'date': month, 'value': value})

        return Response(stat)
