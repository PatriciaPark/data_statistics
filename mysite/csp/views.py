from django.shortcuts import render
from django.http import JsonResponse
from django.db.models import Sum
from csd.models import InvoiceMonthly, InvoiceDaily, Product, Store
from datetime import datetime
import datetime as dt

# Create your views here.
def index(request):
    # html에서 선택한 날짜 받아오기
    year = request.GET.get('input-year')   #2022
    
    if year is None:
        year = datetime.today().year
    
    # select box list
    product = Product.objects.all()
    
    # html에서 선택한 select box value 받아오기
    prdcode = request.GET.get('input-prd')  #상품코드
        
    # get select box value
    getloc = request.GET.get('add-loc')
    getCity = request.GET.get('add-city')
    getStore = request.GET.get('add-str')    
        
    # set select box value
    loc = Store.objects.values('str_loc').distinct()
    city = Store.objects.filter(str_loc=getloc).values('str_city').distinct()
    str = Store.objects.filter(str_loc=getloc, str_city=getCity).values('str_name').order_by('str_name')
    
    # 상단에 표시할 상품명
    prdname = Product.objects.filter(prd_code = prdcode).values_list('prd_name', flat=True)
    
    # read data
    # 지역만 선택
    if getloc != 'all' and (getCity is None or getCity == 'all') and (getStore is None or getStore == 'all'):
        # 데이터
        data = InvoiceDaily.objects.filter(str_code__str_loc=getloc, prd_code = prdcode, inv_d_date__year=year).select_related('prd_code','str_code').values('str_code','str_code__str_city','str_code__str_name','prd_code__prd_name').annotate(Sum('inv_d_sale'))
        # 월별 판매 데이터
        saleJan  = list(InvoiceDaily.objects.filter(str_code__str_loc=getloc, prd_code = prdcode, inv_d_date__gte=dt.date(int(year)-1,12,30), inv_d_date__lte=dt.date(int(year),1,12)).select_related('prd_code','str_code').values('str_code').annotate(Sum('inv_d_sale')))
        saleJan2 = list(InvoiceDaily.objects.filter(str_code__str_loc=getloc, prd_code = prdcode, inv_d_date__gte=dt.date(int(year),1,13), inv_d_date__lte=dt.date(int(year),2,2)).select_related('prd_code','str_code').values('str_code').annotate(Sum('inv_d_sale')))
        saleFeb  = list(InvoiceDaily.objects.filter(str_code__str_loc=getloc, prd_code = prdcode, inv_d_date__gte=dt.date(int(year),2,3), inv_d_date__lte=dt.date(int(year),2,16)).select_related('prd_code','str_code').values('str_code').annotate(Sum('inv_d_sale')))
        saleFeb2 = list(InvoiceDaily.objects.filter(str_code__str_loc=getloc, prd_code = prdcode, inv_d_date__gte=dt.date(int(year),2,17), inv_d_date__lte=dt.date(int(year),3,2)).select_related('prd_code','str_code').values('str_code').annotate(Sum('inv_d_sale')))
        saleMar  = list(InvoiceDaily.objects.filter(str_code__str_loc=getloc, prd_code = prdcode, inv_d_date__gte=dt.date(int(year),3,3), inv_d_date__lte=dt.date(int(year),3,16)).select_related('prd_code','str_code').values('str_code').annotate(Sum('inv_d_sale')))
        saleMar2 = list(InvoiceDaily.objects.filter(str_code__str_loc=getloc, prd_code = prdcode, inv_d_date__gte=dt.date(int(year),3,17), inv_d_date__lte=dt.date(int(year),4,6)).select_related('prd_code','str_code').values('str_code').annotate(Sum('inv_d_sale')))
        saleApr  = list(InvoiceDaily.objects.filter(str_code__str_loc=getloc, prd_code = prdcode, inv_d_date__gte=dt.date(int(year),4,7), inv_d_date__lte=dt.date(int(year),4,20)).select_related('prd_code','str_code').values('str_code').annotate(Sum('inv_d_sale')))
        saleApr2 = list(InvoiceDaily.objects.filter(str_code__str_loc=getloc, prd_code = prdcode, inv_d_date__gte=dt.date(int(year),4,21), inv_d_date__lte=dt.date(int(year),5,4)).select_related('prd_code','str_code').values('str_code').annotate(Sum('inv_d_sale')))
        saleMay  = list(InvoiceDaily.objects.filter(str_code__str_loc=getloc, prd_code = prdcode, inv_d_date__gte=dt.date(int(year),5,5), inv_d_date__lte=dt.date(int(year),5,18)).select_related('prd_code','str_code').values('str_code').annotate(Sum('inv_d_sale')))
        saleMay2 = list(InvoiceDaily.objects.filter(str_code__str_loc=getloc, prd_code = prdcode, inv_d_date__gte=dt.date(int(year),5,19), inv_d_date__lte=dt.date(int(year),6,1)).select_related('prd_code','str_code').values('str_code').annotate(Sum('inv_d_sale')))
        saleJun  = list(InvoiceDaily.objects.filter(str_code__str_loc=getloc, prd_code = prdcode, inv_d_date__gte=dt.date(int(year),6,2), inv_d_date__lte=dt.date(int(year),6,15)).select_related('prd_code','str_code').values('str_code').annotate(Sum('inv_d_sale')))
        saleJun2 = list(InvoiceDaily.objects.filter(str_code__str_loc=getloc, prd_code = prdcode, inv_d_date__gte=dt.date(int(year),6,16), inv_d_date__lte=dt.date(int(year),7,6)).select_related('prd_code','str_code').values('str_code').annotate(Sum('inv_d_sale')))
        saleJul  = list(InvoiceDaily.objects.filter(str_code__str_loc=getloc, prd_code = prdcode, inv_d_date__gte=dt.date(int(year),7,7), inv_d_date__lte=dt.date(int(year),7,20)).select_related('prd_code','str_code').values('str_code').annotate(Sum('inv_d_sale')))
        saleJul2 = list(InvoiceDaily.objects.filter(str_code__str_loc=getloc, prd_code = prdcode, inv_d_date__gte=dt.date(int(year),7,21), inv_d_date__lte=dt.date(int(year),8,10)).select_related('prd_code','str_code').values('str_code').annotate(Sum('inv_d_sale')))
        saleAug  = list(InvoiceDaily.objects.filter(str_code__str_loc=getloc, prd_code = prdcode, inv_d_date__gte=dt.date(int(year),8,11), inv_d_date__lte=dt.date(int(year),8,24)).select_related('prd_code','str_code').values('str_code').annotate(Sum('inv_d_sale')))
        saleAug2 = list(InvoiceDaily.objects.filter(str_code__str_loc=getloc, prd_code = prdcode, inv_d_date__gte=dt.date(int(year),8,25), inv_d_date__lte=dt.date(int(year),9,7)).select_related('prd_code','str_code').values('str_code').annotate(Sum('inv_d_sale')))
        saleSep  = list(InvoiceDaily.objects.filter(str_code__str_loc=getloc, prd_code = prdcode, inv_d_date__gte=dt.date(int(year),9,8), inv_d_date__lte=dt.date(int(year),9,21)).select_related('prd_code','str_code').values('str_code').annotate(Sum('inv_d_sale')))
        saleSep2 = list(InvoiceDaily.objects.filter(str_code__str_loc=getloc, prd_code = prdcode, inv_d_date__gte=dt.date(int(year),9,22), inv_d_date__lte=dt.date(int(year),10,5)).select_related('prd_code','str_code').values('str_code').annotate(Sum('inv_d_sale')))
        saleOct  = list(InvoiceDaily.objects.filter(str_code__str_loc=getloc, prd_code = prdcode, inv_d_date__gte=dt.date(int(year),10,6), inv_d_date__lte=dt.date(int(year),10,19)).select_related('prd_code','str_code').values('str_code').annotate(Sum('inv_d_sale')))
        saleOct2 = list(InvoiceDaily.objects.filter(str_code__str_loc=getloc, prd_code = prdcode, inv_d_date__gte=dt.date(int(year),10,20), inv_d_date__lte=dt.date(int(year),11,2)).select_related('prd_code','str_code').values('str_code').annotate(Sum('inv_d_sale')))
        saleNov  = list(InvoiceDaily.objects.filter(str_code__str_loc=getloc, prd_code = prdcode, inv_d_date__gte=dt.date(int(year),11,3), inv_d_date__lte=dt.date(int(year),11,23)).select_related('prd_code','str_code').values('str_code').annotate(Sum('inv_d_sale')))
        saleNov2 = list(InvoiceDaily.objects.filter(str_code__str_loc=getloc, prd_code = prdcode, inv_d_date__gte=dt.date(int(year),11,24), inv_d_date__lte=dt.date(int(year),12,7)).select_related('prd_code','str_code').values('str_code').annotate(Sum('inv_d_sale')))
        saleDec  = list(InvoiceDaily.objects.filter(str_code__str_loc=getloc, prd_code = prdcode, inv_d_date__gte=dt.date(int(year),12,8), inv_d_date__lte=dt.date(int(year),12,21)).select_related('prd_code','str_code').values('str_code').annotate(Sum('inv_d_sale')))
        saleDec2 = list(InvoiceDaily.objects.filter(str_code__str_loc=getloc, prd_code = prdcode, inv_d_date__gte=dt.date(int(year),12,22), inv_d_date__lte=dt.date(int(year)+1,1,4)).select_related('prd_code','str_code').values('str_code').annotate(Sum('inv_d_sale')))
        # 최하단 총합계 데이터
        totaldata = InvoiceDaily.objects.filter(str_code__str_loc=getloc, prd_code = prdcode, inv_d_date__year=year).select_related('prd_code','str_code').aggregate(Sum('inv_d_sale'))
        # 월별 판매 총합 데이터
        totalsaleJan  = InvoiceDaily.objects.filter(str_code__str_loc=getloc, prd_code = prdcode, inv_d_date__gte=dt.date(int(year)-1,12,30), inv_d_date__lte=dt.date(int(year),1,12)).select_related('prd_code','str_code').values('str_code').aggregate(Sum('inv_d_sale'))
        totalsaleJan2 = InvoiceDaily.objects.filter(str_code__str_loc=getloc, prd_code = prdcode, inv_d_date__gte=dt.date(int(year),1,13), inv_d_date__lte=dt.date(int(year),2,2)).select_related('prd_code','str_code').values('str_code').aggregate(Sum('inv_d_sale'))
        totalsaleFeb  = InvoiceDaily.objects.filter(str_code__str_loc=getloc, prd_code = prdcode, inv_d_date__gte=dt.date(int(year),2,3), inv_d_date__lte=dt.date(int(year),2,16)).select_related('prd_code','str_code').values('str_code').aggregate(Sum('inv_d_sale'))
        totalsaleFeb2 = InvoiceDaily.objects.filter(str_code__str_loc=getloc, prd_code = prdcode, inv_d_date__gte=dt.date(int(year),2,17), inv_d_date__lte=dt.date(int(year),3,2)).select_related('prd_code','str_code').values('str_code').aggregate(Sum('inv_d_sale'))
        totalsaleMar  = InvoiceDaily.objects.filter(str_code__str_loc=getloc, prd_code = prdcode, inv_d_date__gte=dt.date(int(year),3,3), inv_d_date__lte=dt.date(int(year),3,16)).select_related('prd_code','str_code').values('str_code').aggregate(Sum('inv_d_sale'))
        totalsaleMar2 = InvoiceDaily.objects.filter(str_code__str_loc=getloc, prd_code = prdcode, inv_d_date__gte=dt.date(int(year),3,17), inv_d_date__lte=dt.date(int(year),4,6)).select_related('prd_code','str_code').values('str_code').aggregate(Sum('inv_d_sale'))
        totalsaleApr  = InvoiceDaily.objects.filter(str_code__str_loc=getloc, prd_code = prdcode, inv_d_date__gte=dt.date(int(year),4,7), inv_d_date__lte=dt.date(int(year),4,20)).select_related('prd_code','str_code').values('str_code').aggregate(Sum('inv_d_sale'))
        totalsaleApr2 = InvoiceDaily.objects.filter(str_code__str_loc=getloc, prd_code = prdcode, inv_d_date__gte=dt.date(int(year),4,21), inv_d_date__lte=dt.date(int(year),5,4)).select_related('prd_code','str_code').values('str_code').aggregate(Sum('inv_d_sale'))
        totalsaleMay  = InvoiceDaily.objects.filter(str_code__str_loc=getloc, prd_code = prdcode, inv_d_date__gte=dt.date(int(year),5,5), inv_d_date__lte=dt.date(int(year),5,18)).select_related('prd_code','str_code').values('str_code').aggregate(Sum('inv_d_sale'))
        totalsaleMay2 = InvoiceDaily.objects.filter(str_code__str_loc=getloc, prd_code = prdcode, inv_d_date__gte=dt.date(int(year),5,19), inv_d_date__lte=dt.date(int(year),6,1)).select_related('prd_code','str_code').values('str_code').aggregate(Sum('inv_d_sale'))
        totalsaleJun  = InvoiceDaily.objects.filter(str_code__str_loc=getloc, prd_code = prdcode, inv_d_date__gte=dt.date(int(year),6,2), inv_d_date__lte=dt.date(int(year),6,15)).select_related('prd_code','str_code').values('str_code').aggregate(Sum('inv_d_sale'))
        totalsaleJun2 = InvoiceDaily.objects.filter(str_code__str_loc=getloc, prd_code = prdcode, inv_d_date__gte=dt.date(int(year),6,16), inv_d_date__lte=dt.date(int(year),7,6)).select_related('prd_code','str_code').values('str_code').aggregate(Sum('inv_d_sale'))
        totalsaleJul  = InvoiceDaily.objects.filter(str_code__str_loc=getloc, prd_code = prdcode, inv_d_date__gte=dt.date(int(year),7,7), inv_d_date__lte=dt.date(int(year),7,20)).select_related('prd_code','str_code').values('str_code').aggregate(Sum('inv_d_sale'))
        totalsaleJul2 = InvoiceDaily.objects.filter(str_code__str_loc=getloc, prd_code = prdcode, inv_d_date__gte=dt.date(int(year),7,21), inv_d_date__lte=dt.date(int(year),8,10)).select_related('prd_code','str_code').values('str_code').aggregate(Sum('inv_d_sale'))
        totalsaleAug  = InvoiceDaily.objects.filter(str_code__str_loc=getloc, prd_code = prdcode, inv_d_date__gte=dt.date(int(year),8,11), inv_d_date__lte=dt.date(int(year),8,24)).select_related('prd_code','str_code').values('str_code').aggregate(Sum('inv_d_sale'))
        totalsaleAug2 = InvoiceDaily.objects.filter(str_code__str_loc=getloc, prd_code = prdcode, inv_d_date__gte=dt.date(int(year),8,25), inv_d_date__lte=dt.date(int(year),9,7)).select_related('prd_code','str_code').values('str_code').aggregate(Sum('inv_d_sale'))
        totalsaleSep  = InvoiceDaily.objects.filter(str_code__str_loc=getloc, prd_code = prdcode, inv_d_date__gte=dt.date(int(year),9,8), inv_d_date__lte=dt.date(int(year),9,21)).select_related('prd_code','str_code').values('str_code').aggregate(Sum('inv_d_sale'))
        totalsaleSep2 = InvoiceDaily.objects.filter(str_code__str_loc=getloc, prd_code = prdcode, inv_d_date__gte=dt.date(int(year),9,22), inv_d_date__lte=dt.date(int(year),10,5)).select_related('prd_code','str_code').values('str_code').aggregate(Sum('inv_d_sale'))
        totalsaleOct  = InvoiceDaily.objects.filter(str_code__str_loc=getloc, prd_code = prdcode, inv_d_date__gte=dt.date(int(year),10,6), inv_d_date__lte=dt.date(int(year),10,19)).select_related('prd_code','str_code').values('str_code').aggregate(Sum('inv_d_sale'))
        totalsaleOct2 = InvoiceDaily.objects.filter(str_code__str_loc=getloc, prd_code = prdcode, inv_d_date__gte=dt.date(int(year),10,20), inv_d_date__lte=dt.date(int(year),11,1)).select_related('prd_code','str_code').values('str_code').aggregate(Sum('inv_d_sale'))
        totalsaleNov  = InvoiceDaily.objects.filter(str_code__str_loc=getloc, prd_code = prdcode, inv_d_date__gte=dt.date(int(year),11,3), inv_d_date__lte=dt.date(int(year),11,23)).select_related('prd_code','str_code').values('str_code').aggregate(Sum('inv_d_sale'))
        totalsaleNov2 = InvoiceDaily.objects.filter(str_code__str_loc=getloc, prd_code = prdcode, inv_d_date__gte=dt.date(int(year),11,24), inv_d_date__lte=dt.date(int(year),12,7)).select_related('prd_code','str_code').values('str_code').aggregate(Sum('inv_d_sale'))
        totalsaleDec  = InvoiceDaily.objects.filter(str_code__str_loc=getloc, prd_code = prdcode, inv_d_date__gte=dt.date(int(year),12,8), inv_d_date__lte=dt.date(int(year),12,21)).select_related('prd_code','str_code').values('str_code').aggregate(Sum('inv_d_sale'))
        totalsaleDec2 = InvoiceDaily.objects.filter(str_code__str_loc=getloc, prd_code = prdcode, inv_d_date__gte=dt.date(int(year),12,22), inv_d_date__lte=dt.date(int(year)+1,1,4)).select_related('prd_code','str_code').values('str_code').aggregate(Sum('inv_d_sale'))     
        
    # 지역 및 시까지 선택
    elif getloc != 'all' and getCity is not None and (getStore is None or getStore == 'all'):
        # 데이터
        data = InvoiceDaily.objects.filter(str_code__str_loc=getloc, str_code__str_city=getCity, prd_code = prdcode, inv_d_date__year=year).select_related('prd_code','str_code').values('str_code','str_code__str_city','str_code__str_name','prd_code__prd_name').annotate(Sum('inv_d_sale'))
        # 월별 판매 데이터
        saleJan  = list(InvoiceDaily.objects.filter(str_code__str_loc=getloc, str_code__str_city=getCity, prd_code = prdcode, inv_d_date__gte=dt.date(int(year)-1,12,30), inv_d_date__lte=dt.date(int(year),1,12)).select_related('prd_code','str_code').values('str_code').annotate(Sum('inv_d_sale')))
        saleJan2 = list(InvoiceDaily.objects.filter(str_code__str_loc=getloc, str_code__str_city=getCity, prd_code = prdcode, inv_d_date__gte=dt.date(int(year),1,13), inv_d_date__lte=dt.date(int(year),2,2)).select_related('prd_code','str_code').values('str_code').annotate(Sum('inv_d_sale')))
        saleFeb  = list(InvoiceDaily.objects.filter(str_code__str_loc=getloc, str_code__str_city=getCity, prd_code = prdcode, inv_d_date__gte=dt.date(int(year),2,3), inv_d_date__lte=dt.date(int(year),2,16)).select_related('prd_code','str_code').values('str_code').annotate(Sum('inv_d_sale')))
        saleFeb2 = list(InvoiceDaily.objects.filter(str_code__str_loc=getloc, str_code__str_city=getCity, prd_code = prdcode, inv_d_date__gte=dt.date(int(year),2,17), inv_d_date__lte=dt.date(int(year),3,2)).select_related('prd_code','str_code').values('str_code').annotate(Sum('inv_d_sale')))
        saleMar  = list(InvoiceDaily.objects.filter(str_code__str_loc=getloc, str_code__str_city=getCity, prd_code = prdcode, inv_d_date__gte=dt.date(int(year),3,3), inv_d_date__lte=dt.date(int(year),3,16)).select_related('prd_code','str_code').values('str_code').annotate(Sum('inv_d_sale')))
        saleMar2 = list(InvoiceDaily.objects.filter(str_code__str_loc=getloc, str_code__str_city=getCity, prd_code = prdcode, inv_d_date__gte=dt.date(int(year),3,17), inv_d_date__lte=dt.date(int(year),4,6)).select_related('prd_code','str_code').values('str_code').annotate(Sum('inv_d_sale')))
        saleApr  = list(InvoiceDaily.objects.filter(str_code__str_loc=getloc, str_code__str_city=getCity, prd_code = prdcode, inv_d_date__gte=dt.date(int(year),4,7), inv_d_date__lte=dt.date(int(year),4,20)).select_related('prd_code','str_code').values('str_code').annotate(Sum('inv_d_sale')))
        saleApr2 = list(InvoiceDaily.objects.filter(str_code__str_loc=getloc, str_code__str_city=getCity, prd_code = prdcode, inv_d_date__gte=dt.date(int(year),4,21), inv_d_date__lte=dt.date(int(year),5,4)).select_related('prd_code','str_code').values('str_code').annotate(Sum('inv_d_sale')))
        saleMay  = list(InvoiceDaily.objects.filter(str_code__str_loc=getloc, str_code__str_city=getCity, prd_code = prdcode, inv_d_date__gte=dt.date(int(year),5,5), inv_d_date__lte=dt.date(int(year),5,18)).select_related('prd_code','str_code').values('str_code').annotate(Sum('inv_d_sale')))
        saleMay2 = list(InvoiceDaily.objects.filter(str_code__str_loc=getloc, str_code__str_city=getCity, prd_code = prdcode, inv_d_date__gte=dt.date(int(year),5,19), inv_d_date__lte=dt.date(int(year),6,1)).select_related('prd_code','str_code').values('str_code').annotate(Sum('inv_d_sale')))
        saleJun  = list(InvoiceDaily.objects.filter(str_code__str_loc=getloc, str_code__str_city=getCity, prd_code = prdcode, inv_d_date__gte=dt.date(int(year),6,2), inv_d_date__lte=dt.date(int(year),6,15)).select_related('prd_code','str_code').values('str_code').annotate(Sum('inv_d_sale')))
        saleJun2 = list(InvoiceDaily.objects.filter(str_code__str_loc=getloc, str_code__str_city=getCity, prd_code = prdcode, inv_d_date__gte=dt.date(int(year),6,16), inv_d_date__lte=dt.date(int(year),7,6)).select_related('prd_code','str_code').values('str_code').annotate(Sum('inv_d_sale')))
        saleJul  = list(InvoiceDaily.objects.filter(str_code__str_loc=getloc, str_code__str_city=getCity, prd_code = prdcode, inv_d_date__gte=dt.date(int(year),7,7), inv_d_date__lte=dt.date(int(year),7,20)).select_related('prd_code','str_code').values('str_code').annotate(Sum('inv_d_sale')))
        saleJul2 = list(InvoiceDaily.objects.filter(str_code__str_loc=getloc, str_code__str_city=getCity, prd_code = prdcode, inv_d_date__gte=dt.date(int(year),7,21), inv_d_date__lte=dt.date(int(year),8,10)).select_related('prd_code','str_code').values('str_code').annotate(Sum('inv_d_sale')))
        saleAug  = list(InvoiceDaily.objects.filter(str_code__str_loc=getloc, str_code__str_city=getCity, prd_code = prdcode, inv_d_date__gte=dt.date(int(year),8,11), inv_d_date__lte=dt.date(int(year),8,24)).select_related('prd_code','str_code').values('str_code').annotate(Sum('inv_d_sale')))
        saleAug2 = list(InvoiceDaily.objects.filter(str_code__str_loc=getloc, str_code__str_city=getCity, prd_code = prdcode, inv_d_date__gte=dt.date(int(year),8,25), inv_d_date__lte=dt.date(int(year),9,7)).select_related('prd_code','str_code').values('str_code').annotate(Sum('inv_d_sale')))
        saleSep  = list(InvoiceDaily.objects.filter(str_code__str_loc=getloc, str_code__str_city=getCity, prd_code = prdcode, inv_d_date__gte=dt.date(int(year),9,8), inv_d_date__lte=dt.date(int(year),9,21)).select_related('prd_code','str_code').values('str_code').annotate(Sum('inv_d_sale')))
        saleSep2 = list(InvoiceDaily.objects.filter(str_code__str_loc=getloc, str_code__str_city=getCity, prd_code = prdcode, inv_d_date__gte=dt.date(int(year),9,22), inv_d_date__lte=dt.date(int(year),10,5)).select_related('prd_code','str_code').values('str_code').annotate(Sum('inv_d_sale')))
        saleOct  = list(InvoiceDaily.objects.filter(str_code__str_loc=getloc, str_code__str_city=getCity, prd_code = prdcode, inv_d_date__gte=dt.date(int(year),10,6), inv_d_date__lte=dt.date(int(year),10,19)).select_related('prd_code','str_code').values('str_code').annotate(Sum('inv_d_sale')))
        saleOct2 = list(InvoiceDaily.objects.filter(str_code__str_loc=getloc, str_code__str_city=getCity, prd_code = prdcode, inv_d_date__gte=dt.date(int(year),10,20), inv_d_date__lte=dt.date(int(year),11,2)).select_related('prd_code','str_code').values('str_code').annotate(Sum('inv_d_sale')))
        saleNov  = list(InvoiceDaily.objects.filter(str_code__str_loc=getloc, str_code__str_city=getCity, prd_code = prdcode, inv_d_date__gte=dt.date(int(year),11,3), inv_d_date__lte=dt.date(int(year),11,23)).select_related('prd_code','str_code').values('str_code').annotate(Sum('inv_d_sale')))
        saleNov2 = list(InvoiceDaily.objects.filter(str_code__str_loc=getloc, str_code__str_city=getCity, prd_code = prdcode, inv_d_date__gte=dt.date(int(year),11,24), inv_d_date__lte=dt.date(int(year),12,7)).select_related('prd_code','str_code').values('str_code').annotate(Sum('inv_d_sale')))
        saleDec  = list(InvoiceDaily.objects.filter(str_code__str_loc=getloc, str_code__str_city=getCity, prd_code = prdcode, inv_d_date__gte=dt.date(int(year),12,8), inv_d_date__lte=dt.date(int(year),12,21)).select_related('prd_code','str_code').values('str_code').annotate(Sum('inv_d_sale')))
        saleDec2 = list(InvoiceDaily.objects.filter(str_code__str_loc=getloc, str_code__str_city=getCity, prd_code = prdcode, inv_d_date__gte=dt.date(int(year),12,22), inv_d_date__lte=dt.date(int(year)+1,1,4)).select_related('prd_code','str_code').values('str_code').annotate(Sum('inv_d_sale')))
        # 최하단 총합계 데이터
        totaldata = InvoiceDaily.objects.filter(str_code__str_loc=getloc, str_code__str_city=getCity, prd_code = prdcode, inv_d_date__year=year).select_related('prd_code','str_code').aggregate(Sum('inv_d_sale'))
        # 월별 판매 총합 데이터
        totalsaleJan  = InvoiceDaily.objects.filter(str_code__str_loc=getloc, str_code__str_city=getCity, prd_code = prdcode, inv_d_date__gte=dt.date(int(year)-1,12,30), inv_d_date__lte=dt.date(int(year),1,12)).select_related('prd_code','str_code').values('str_code').aggregate(Sum('inv_d_sale'))
        totalsaleJan2 = InvoiceDaily.objects.filter(str_code__str_loc=getloc, str_code__str_city=getCity, prd_code = prdcode, inv_d_date__gte=dt.date(int(year),1,13), inv_d_date__lte=dt.date(int(year),2,2)).select_related('prd_code','str_code').values('str_code').aggregate(Sum('inv_d_sale'))
        totalsaleFeb  = InvoiceDaily.objects.filter(str_code__str_loc=getloc, str_code__str_city=getCity, prd_code = prdcode, inv_d_date__gte=dt.date(int(year),2,3), inv_d_date__lte=dt.date(int(year),2,16)).select_related('prd_code','str_code').values('str_code').aggregate(Sum('inv_d_sale'))
        totalsaleFeb2 = InvoiceDaily.objects.filter(str_code__str_loc=getloc, str_code__str_city=getCity, prd_code = prdcode, inv_d_date__gte=dt.date(int(year),2,17), inv_d_date__lte=dt.date(int(year),3,2)).select_related('prd_code','str_code').values('str_code').aggregate(Sum('inv_d_sale'))
        totalsaleMar  = InvoiceDaily.objects.filter(str_code__str_loc=getloc, str_code__str_city=getCity, prd_code = prdcode, inv_d_date__gte=dt.date(int(year),3,3), inv_d_date__lte=dt.date(int(year),3,16)).select_related('prd_code','str_code').values('str_code').aggregate(Sum('inv_d_sale'))
        totalsaleMar2 = InvoiceDaily.objects.filter(str_code__str_loc=getloc, str_code__str_city=getCity, prd_code = prdcode, inv_d_date__gte=dt.date(int(year),3,17), inv_d_date__lte=dt.date(int(year),4,6)).select_related('prd_code','str_code').values('str_code').aggregate(Sum('inv_d_sale'))
        totalsaleApr  = InvoiceDaily.objects.filter(str_code__str_loc=getloc, str_code__str_city=getCity, prd_code = prdcode, inv_d_date__gte=dt.date(int(year),4,7), inv_d_date__lte=dt.date(int(year),4,20)).select_related('prd_code','str_code').values('str_code').aggregate(Sum('inv_d_sale'))
        totalsaleApr2 = InvoiceDaily.objects.filter(str_code__str_loc=getloc, str_code__str_city=getCity, prd_code = prdcode, inv_d_date__gte=dt.date(int(year),4,21), inv_d_date__lte=dt.date(int(year),5,4)).select_related('prd_code','str_code').values('str_code').aggregate(Sum('inv_d_sale'))
        totalsaleMay  = InvoiceDaily.objects.filter(str_code__str_loc=getloc, str_code__str_city=getCity, prd_code = prdcode, inv_d_date__gte=dt.date(int(year),5,5), inv_d_date__lte=dt.date(int(year),5,18)).select_related('prd_code','str_code').values('str_code').aggregate(Sum('inv_d_sale'))
        totalsaleMay2 = InvoiceDaily.objects.filter(str_code__str_loc=getloc, str_code__str_city=getCity, prd_code = prdcode, inv_d_date__gte=dt.date(int(year),5,19), inv_d_date__lte=dt.date(int(year),6,1)).select_related('prd_code','str_code').values('str_code').aggregate(Sum('inv_d_sale'))
        totalsaleJun  = InvoiceDaily.objects.filter(str_code__str_loc=getloc, str_code__str_city=getCity, prd_code = prdcode, inv_d_date__gte=dt.date(int(year),6,2), inv_d_date__lte=dt.date(int(year),6,15)).select_related('prd_code','str_code').values('str_code').aggregate(Sum('inv_d_sale'))
        totalsaleJun2 = InvoiceDaily.objects.filter(str_code__str_loc=getloc, str_code__str_city=getCity, prd_code = prdcode, inv_d_date__gte=dt.date(int(year),6,16), inv_d_date__lte=dt.date(int(year),7,6)).select_related('prd_code','str_code').values('str_code').aggregate(Sum('inv_d_sale'))
        totalsaleJul  = InvoiceDaily.objects.filter(str_code__str_loc=getloc, str_code__str_city=getCity, prd_code = prdcode, inv_d_date__gte=dt.date(int(year),7,7), inv_d_date__lte=dt.date(int(year),7,20)).select_related('prd_code','str_code').values('str_code').aggregate(Sum('inv_d_sale'))
        totalsaleJul2 = InvoiceDaily.objects.filter(str_code__str_loc=getloc, str_code__str_city=getCity, prd_code = prdcode, inv_d_date__gte=dt.date(int(year),7,21), inv_d_date__lte=dt.date(int(year),8,10)).select_related('prd_code','str_code').values('str_code').aggregate(Sum('inv_d_sale'))
        totalsaleAug  = InvoiceDaily.objects.filter(str_code__str_loc=getloc, str_code__str_city=getCity, prd_code = prdcode, inv_d_date__gte=dt.date(int(year),8,11), inv_d_date__lte=dt.date(int(year),8,24)).select_related('prd_code','str_code').values('str_code').aggregate(Sum('inv_d_sale'))
        totalsaleAug2 = InvoiceDaily.objects.filter(str_code__str_loc=getloc, str_code__str_city=getCity, prd_code = prdcode, inv_d_date__gte=dt.date(int(year),8,25), inv_d_date__lte=dt.date(int(year),9,7)).select_related('prd_code','str_code').values('str_code').aggregate(Sum('inv_d_sale'))
        totalsaleSep  = InvoiceDaily.objects.filter(str_code__str_loc=getloc, str_code__str_city=getCity, prd_code = prdcode, inv_d_date__gte=dt.date(int(year),9,8), inv_d_date__lte=dt.date(int(year),9,21)).select_related('prd_code','str_code').values('str_code').aggregate(Sum('inv_d_sale'))
        totalsaleSep2 = InvoiceDaily.objects.filter(str_code__str_loc=getloc, str_code__str_city=getCity, prd_code = prdcode, inv_d_date__gte=dt.date(int(year),9,22), inv_d_date__lte=dt.date(int(year),10,5)).select_related('prd_code','str_code').values('str_code').aggregate(Sum('inv_d_sale'))
        totalsaleOct  = InvoiceDaily.objects.filter(str_code__str_loc=getloc, str_code__str_city=getCity, prd_code = prdcode, inv_d_date__gte=dt.date(int(year),10,6), inv_d_date__lte=dt.date(int(year),10,19)).select_related('prd_code','str_code').values('str_code').aggregate(Sum('inv_d_sale'))
        totalsaleOct2 = InvoiceDaily.objects.filter(str_code__str_loc=getloc, str_code__str_city=getCity, prd_code = prdcode, inv_d_date__gte=dt.date(int(year),10,20), inv_d_date__lte=dt.date(int(year),11,1)).select_related('prd_code','str_code').values('str_code').aggregate(Sum('inv_d_sale'))
        totalsaleNov  = InvoiceDaily.objects.filter(str_code__str_loc=getloc, str_code__str_city=getCity, prd_code = prdcode, inv_d_date__gte=dt.date(int(year),11,3), inv_d_date__lte=dt.date(int(year),11,23)).select_related('prd_code','str_code').values('str_code').aggregate(Sum('inv_d_sale'))
        totalsaleNov2 = InvoiceDaily.objects.filter(str_code__str_loc=getloc, str_code__str_city=getCity, prd_code = prdcode, inv_d_date__gte=dt.date(int(year),11,24), inv_d_date__lte=dt.date(int(year),12,7)).select_related('prd_code','str_code').values('str_code').aggregate(Sum('inv_d_sale'))
        totalsaleDec  = InvoiceDaily.objects.filter(str_code__str_loc=getloc, str_code__str_city=getCity, prd_code = prdcode, inv_d_date__gte=dt.date(int(year),12,8), inv_d_date__lte=dt.date(int(year),12,21)).select_related('prd_code','str_code').values('str_code').aggregate(Sum('inv_d_sale'))
        totalsaleDec2 = InvoiceDaily.objects.filter(str_code__str_loc=getloc, str_code__str_city=getCity, prd_code = prdcode, inv_d_date__gte=dt.date(int(year),12,22), inv_d_date__lte=dt.date(int(year)+1,1,4)).select_related('prd_code','str_code').values('str_code').aggregate(Sum('inv_d_sale'))
            
    #지역, 시, 매장 선택
    elif getloc != 'all' and getCity is not None and getStore is not None:
        # 데이터
        data = InvoiceDaily.objects.filter(str_code__str_loc=getloc, str_code__str_city=getCity, str_code__str_name=getStore, prd_code = prdcode, inv_d_date__year=year).select_related('prd_code','str_code').values('str_code','str_code__str_city','str_code__str_name','prd_code__prd_name').annotate(Sum('inv_d_sale'))
        # 월별 판매 데이터
        saleJan  = list(InvoiceDaily.objects.filter(str_code__str_loc=getloc, str_code__str_city=getCity, str_code__str_name=getStore, prd_code = prdcode, inv_d_date__gte=dt.date(int(year)-1,12,30), inv_d_date__lte=dt.date(int(year),1,12)).select_related('prd_code','str_code').values('str_code').annotate(Sum('inv_d_sale')))
        saleJan2 = list(InvoiceDaily.objects.filter(str_code__str_loc=getloc, str_code__str_city=getCity, str_code__str_name=getStore, prd_code = prdcode, inv_d_date__gte=dt.date(int(year),1,13), inv_d_date__lte=dt.date(int(year),2,2)).select_related('prd_code','str_code').values('str_code').annotate(Sum('inv_d_sale')))
        saleFeb  = list(InvoiceDaily.objects.filter(str_code__str_loc=getloc, str_code__str_city=getCity, str_code__str_name=getStore, prd_code = prdcode, inv_d_date__gte=dt.date(int(year),2,3), inv_d_date__lte=dt.date(int(year),2,16)).select_related('prd_code','str_code').values('str_code').annotate(Sum('inv_d_sale')))
        saleFeb2 = list(InvoiceDaily.objects.filter(str_code__str_loc=getloc, str_code__str_city=getCity, str_code__str_name=getStore, prd_code = prdcode, inv_d_date__gte=dt.date(int(year),2,17), inv_d_date__lte=dt.date(int(year),3,2)).select_related('prd_code','str_code').values('str_code').annotate(Sum('inv_d_sale')))
        saleMar  = list(InvoiceDaily.objects.filter(str_code__str_loc=getloc, str_code__str_city=getCity, str_code__str_name=getStore, prd_code = prdcode, inv_d_date__gte=dt.date(int(year),3,3), inv_d_date__lte=dt.date(int(year),3,16)).select_related('prd_code','str_code').values('str_code').annotate(Sum('inv_d_sale')))
        saleMar2 = list(InvoiceDaily.objects.filter(str_code__str_loc=getloc, str_code__str_city=getCity, str_code__str_name=getStore, prd_code = prdcode, inv_d_date__gte=dt.date(int(year),3,17), inv_d_date__lte=dt.date(int(year),4,6)).select_related('prd_code','str_code').values('str_code').annotate(Sum('inv_d_sale')))
        saleApr  = list(InvoiceDaily.objects.filter(str_code__str_loc=getloc, str_code__str_city=getCity, str_code__str_name=getStore, prd_code = prdcode, inv_d_date__gte=dt.date(int(year),4,7), inv_d_date__lte=dt.date(int(year),4,20)).select_related('prd_code','str_code').values('str_code').annotate(Sum('inv_d_sale')))
        saleApr2 = list(InvoiceDaily.objects.filter(str_code__str_loc=getloc, str_code__str_city=getCity, str_code__str_name=getStore, prd_code = prdcode, inv_d_date__gte=dt.date(int(year),4,21), inv_d_date__lte=dt.date(int(year),5,4)).select_related('prd_code','str_code').values('str_code').annotate(Sum('inv_d_sale')))
        saleMay  = list(InvoiceDaily.objects.filter(str_code__str_loc=getloc, str_code__str_city=getCity, str_code__str_name=getStore, prd_code = prdcode, inv_d_date__gte=dt.date(int(year),5,5), inv_d_date__lte=dt.date(int(year),5,18)).select_related('prd_code','str_code').values('str_code').annotate(Sum('inv_d_sale')))
        saleMay2 = list(InvoiceDaily.objects.filter(str_code__str_loc=getloc, str_code__str_city=getCity, str_code__str_name=getStore, prd_code = prdcode, inv_d_date__gte=dt.date(int(year),5,19), inv_d_date__lte=dt.date(int(year),6,1)).select_related('prd_code','str_code').values('str_code').annotate(Sum('inv_d_sale')))
        saleJun  = list(InvoiceDaily.objects.filter(str_code__str_loc=getloc, str_code__str_city=getCity, str_code__str_name=getStore, prd_code = prdcode, inv_d_date__gte=dt.date(int(year),6,2), inv_d_date__lte=dt.date(int(year),6,15)).select_related('prd_code','str_code').values('str_code').annotate(Sum('inv_d_sale')))
        saleJun2 = list(InvoiceDaily.objects.filter(str_code__str_loc=getloc, str_code__str_city=getCity, str_code__str_name=getStore, prd_code = prdcode, inv_d_date__gte=dt.date(int(year),6,16), inv_d_date__lte=dt.date(int(year),7,6)).select_related('prd_code','str_code').values('str_code').annotate(Sum('inv_d_sale')))
        saleJul  = list(InvoiceDaily.objects.filter(str_code__str_loc=getloc, str_code__str_city=getCity, str_code__str_name=getStore, prd_code = prdcode, inv_d_date__gte=dt.date(int(year),7,7), inv_d_date__lte=dt.date(int(year),7,20)).select_related('prd_code','str_code').values('str_code').annotate(Sum('inv_d_sale')))
        saleJul2 = list(InvoiceDaily.objects.filter(str_code__str_loc=getloc, str_code__str_city=getCity, str_code__str_name=getStore, prd_code = prdcode, inv_d_date__gte=dt.date(int(year),7,21), inv_d_date__lte=dt.date(int(year),8,10)).select_related('prd_code','str_code').values('str_code').annotate(Sum('inv_d_sale')))
        saleAug  = list(InvoiceDaily.objects.filter(str_code__str_loc=getloc, str_code__str_city=getCity, str_code__str_name=getStore, prd_code = prdcode, inv_d_date__gte=dt.date(int(year),8,11), inv_d_date__lte=dt.date(int(year),8,24)).select_related('prd_code','str_code').values('str_code').annotate(Sum('inv_d_sale')))
        saleAug2 = list(InvoiceDaily.objects.filter(str_code__str_loc=getloc, str_code__str_city=getCity, str_code__str_name=getStore, prd_code = prdcode, inv_d_date__gte=dt.date(int(year),8,25), inv_d_date__lte=dt.date(int(year),9,7)).select_related('prd_code','str_code').values('str_code').annotate(Sum('inv_d_sale')))
        saleSep  = list(InvoiceDaily.objects.filter(str_code__str_loc=getloc, str_code__str_city=getCity, str_code__str_name=getStore, prd_code = prdcode, inv_d_date__gte=dt.date(int(year),9,8), inv_d_date__lte=dt.date(int(year),9,21)).select_related('prd_code','str_code').values('str_code').annotate(Sum('inv_d_sale')))
        saleSep2 = list(InvoiceDaily.objects.filter(str_code__str_loc=getloc, str_code__str_city=getCity, str_code__str_name=getStore, prd_code = prdcode, inv_d_date__gte=dt.date(int(year),9,22), inv_d_date__lte=dt.date(int(year),10,5)).select_related('prd_code','str_code').values('str_code').annotate(Sum('inv_d_sale')))
        saleOct  = list(InvoiceDaily.objects.filter(str_code__str_loc=getloc, str_code__str_city=getCity, str_code__str_name=getStore, prd_code = prdcode, inv_d_date__gte=dt.date(int(year),10,6), inv_d_date__lte=dt.date(int(year),10,19)).select_related('prd_code','str_code').values('str_code').annotate(Sum('inv_d_sale')))
        saleOct2 = list(InvoiceDaily.objects.filter(str_code__str_loc=getloc, str_code__str_city=getCity, str_code__str_name=getStore, prd_code = prdcode, inv_d_date__gte=dt.date(int(year),10,20), inv_d_date__lte=dt.date(int(year),11,2)).select_related('prd_code','str_code').values('str_code').annotate(Sum('inv_d_sale')))
        saleNov  = list(InvoiceDaily.objects.filter(str_code__str_loc=getloc, str_code__str_city=getCity, str_code__str_name=getStore, prd_code = prdcode, inv_d_date__gte=dt.date(int(year),11,3), inv_d_date__lte=dt.date(int(year),11,23)).select_related('prd_code','str_code').values('str_code').annotate(Sum('inv_d_sale')))
        saleNov2 = list(InvoiceDaily.objects.filter(str_code__str_loc=getloc, str_code__str_city=getCity, str_code__str_name=getStore, prd_code = prdcode, inv_d_date__gte=dt.date(int(year),11,24), inv_d_date__lte=dt.date(int(year),12,7)).select_related('prd_code','str_code').values('str_code').annotate(Sum('inv_d_sale')))
        saleDec  = list(InvoiceDaily.objects.filter(str_code__str_loc=getloc, str_code__str_city=getCity, str_code__str_name=getStore, prd_code = prdcode, inv_d_date__gte=dt.date(int(year),12,8), inv_d_date__lte=dt.date(int(year),12,21)).select_related('prd_code','str_code').values('str_code').annotate(Sum('inv_d_sale')))
        saleDec2 = list(InvoiceDaily.objects.filter(str_code__str_loc=getloc, str_code__str_city=getCity, str_code__str_name=getStore, prd_code = prdcode, inv_d_date__gte=dt.date(int(year),12,22), inv_d_date__lte=dt.date(int(year)+1,1,4)).select_related('prd_code','str_code').values('str_code').annotate(Sum('inv_d_sale')))
        # 최하단 총합계 데이터
        totaldata = InvoiceDaily.objects.filter(str_code__str_loc=getloc, str_code__str_city=getCity, str_code__str_name=getStore, prd_code = prdcode, inv_d_date__year=year).select_related('prd_code','str_code').aggregate(Sum('inv_d_sale'))
        # 월별 판매 총합 데이터
        totalsaleJan  = InvoiceDaily.objects.filter(str_code__str_loc=getloc, str_code__str_city=getCity, str_code__str_name=getStore, prd_code = prdcode, inv_d_date__gte=dt.date(int(year)-1,12,30), inv_d_date__lte=dt.date(int(year),1,12)).select_related('prd_code','str_code').values('str_code').aggregate(Sum('inv_d_sale'))
        totalsaleJan2 = InvoiceDaily.objects.filter(str_code__str_loc=getloc, str_code__str_city=getCity, str_code__str_name=getStore, prd_code = prdcode, inv_d_date__gte=dt.date(int(year),1,13), inv_d_date__lte=dt.date(int(year),2,2)).select_related('prd_code','str_code').values('str_code').aggregate(Sum('inv_d_sale'))
        totalsaleFeb  = InvoiceDaily.objects.filter(str_code__str_loc=getloc, str_code__str_city=getCity, str_code__str_name=getStore, prd_code = prdcode, inv_d_date__gte=dt.date(int(year),2,3), inv_d_date__lte=dt.date(int(year),2,16)).select_related('prd_code','str_code').values('str_code').aggregate(Sum('inv_d_sale'))
        totalsaleFeb2 = InvoiceDaily.objects.filter(str_code__str_loc=getloc, str_code__str_city=getCity, str_code__str_name=getStore, prd_code = prdcode, inv_d_date__gte=dt.date(int(year),2,17), inv_d_date__lte=dt.date(int(year),3,2)).select_related('prd_code','str_code').values('str_code').aggregate(Sum('inv_d_sale'))
        totalsaleMar  = InvoiceDaily.objects.filter(str_code__str_loc=getloc, str_code__str_city=getCity, str_code__str_name=getStore, prd_code = prdcode, inv_d_date__gte=dt.date(int(year),3,3), inv_d_date__lte=dt.date(int(year),3,16)).select_related('prd_code','str_code').values('str_code').aggregate(Sum('inv_d_sale'))
        totalsaleMar2 = InvoiceDaily.objects.filter(str_code__str_loc=getloc, str_code__str_city=getCity, str_code__str_name=getStore, prd_code = prdcode, inv_d_date__gte=dt.date(int(year),3,17), inv_d_date__lte=dt.date(int(year),4,6)).select_related('prd_code','str_code').values('str_code').aggregate(Sum('inv_d_sale'))
        totalsaleApr  = InvoiceDaily.objects.filter(str_code__str_loc=getloc, str_code__str_city=getCity, str_code__str_name=getStore, prd_code = prdcode, inv_d_date__gte=dt.date(int(year),4,7), inv_d_date__lte=dt.date(int(year),4,20)).select_related('prd_code','str_code').values('str_code').aggregate(Sum('inv_d_sale'))
        totalsaleApr2 = InvoiceDaily.objects.filter(str_code__str_loc=getloc, str_code__str_city=getCity, str_code__str_name=getStore, prd_code = prdcode, inv_d_date__gte=dt.date(int(year),4,21), inv_d_date__lte=dt.date(int(year),5,4)).select_related('prd_code','str_code').values('str_code').aggregate(Sum('inv_d_sale'))
        totalsaleMay  = InvoiceDaily.objects.filter(str_code__str_loc=getloc, str_code__str_city=getCity, str_code__str_name=getStore, prd_code = prdcode, inv_d_date__gte=dt.date(int(year),5,5), inv_d_date__lte=dt.date(int(year),5,18)).select_related('prd_code','str_code').values('str_code').aggregate(Sum('inv_d_sale'))
        totalsaleMay2 = InvoiceDaily.objects.filter(str_code__str_loc=getloc, str_code__str_city=getCity, str_code__str_name=getStore, prd_code = prdcode, inv_d_date__gte=dt.date(int(year),5,19), inv_d_date__lte=dt.date(int(year),6,1)).select_related('prd_code','str_code').values('str_code').aggregate(Sum('inv_d_sale'))
        totalsaleJun  = InvoiceDaily.objects.filter(str_code__str_loc=getloc, str_code__str_city=getCity, str_code__str_name=getStore, prd_code = prdcode, inv_d_date__gte=dt.date(int(year),6,2), inv_d_date__lte=dt.date(int(year),6,15)).select_related('prd_code','str_code').values('str_code').aggregate(Sum('inv_d_sale'))
        totalsaleJun2 = InvoiceDaily.objects.filter(str_code__str_loc=getloc, str_code__str_city=getCity, str_code__str_name=getStore, prd_code = prdcode, inv_d_date__gte=dt.date(int(year),6,16), inv_d_date__lte=dt.date(int(year),7,6)).select_related('prd_code','str_code').values('str_code').aggregate(Sum('inv_d_sale'))
        totalsaleJul  = InvoiceDaily.objects.filter(str_code__str_loc=getloc, str_code__str_city=getCity, str_code__str_name=getStore, prd_code = prdcode, inv_d_date__gte=dt.date(int(year),7,7), inv_d_date__lte=dt.date(int(year),7,20)).select_related('prd_code','str_code').values('str_code').aggregate(Sum('inv_d_sale'))
        totalsaleJul2 = InvoiceDaily.objects.filter(str_code__str_loc=getloc, str_code__str_city=getCity, str_code__str_name=getStore, prd_code = prdcode, inv_d_date__gte=dt.date(int(year),7,21), inv_d_date__lte=dt.date(int(year),8,10)).select_related('prd_code','str_code').values('str_code').aggregate(Sum('inv_d_sale'))
        totalsaleAug  = InvoiceDaily.objects.filter(str_code__str_loc=getloc, str_code__str_city=getCity, str_code__str_name=getStore, prd_code = prdcode, inv_d_date__gte=dt.date(int(year),8,11), inv_d_date__lte=dt.date(int(year),8,24)).select_related('prd_code','str_code').values('str_code').aggregate(Sum('inv_d_sale'))
        totalsaleAug2 = InvoiceDaily.objects.filter(str_code__str_loc=getloc, str_code__str_city=getCity, str_code__str_name=getStore, prd_code = prdcode, inv_d_date__gte=dt.date(int(year),8,25), inv_d_date__lte=dt.date(int(year),9,7)).select_related('prd_code','str_code').values('str_code').aggregate(Sum('inv_d_sale'))
        totalsaleSep  = InvoiceDaily.objects.filter(str_code__str_loc=getloc, str_code__str_city=getCity, str_code__str_name=getStore, prd_code = prdcode, inv_d_date__gte=dt.date(int(year),9,8), inv_d_date__lte=dt.date(int(year),9,21)).select_related('prd_code','str_code').values('str_code').aggregate(Sum('inv_d_sale'))
        totalsaleSep2 = InvoiceDaily.objects.filter(str_code__str_loc=getloc, str_code__str_city=getCity, str_code__str_name=getStore, prd_code = prdcode, inv_d_date__gte=dt.date(int(year),9,22), inv_d_date__lte=dt.date(int(year),10,5)).select_related('prd_code','str_code').values('str_code').aggregate(Sum('inv_d_sale'))
        totalsaleOct  = InvoiceDaily.objects.filter(str_code__str_loc=getloc, str_code__str_city=getCity, str_code__str_name=getStore, prd_code = prdcode, inv_d_date__gte=dt.date(int(year),10,6), inv_d_date__lte=dt.date(int(year),10,19)).select_related('prd_code','str_code').values('str_code').aggregate(Sum('inv_d_sale'))
        totalsaleOct2 = InvoiceDaily.objects.filter(str_code__str_loc=getloc, str_code__str_city=getCity, str_code__str_name=getStore, prd_code = prdcode, inv_d_date__gte=dt.date(int(year),10,20), inv_d_date__lte=dt.date(int(year),11,1)).select_related('prd_code','str_code').values('str_code').aggregate(Sum('inv_d_sale'))
        totalsaleNov  = InvoiceDaily.objects.filter(str_code__str_loc=getloc, str_code__str_city=getCity, str_code__str_name=getStore, prd_code = prdcode, inv_d_date__gte=dt.date(int(year),11,3), inv_d_date__lte=dt.date(int(year),11,23)).select_related('prd_code','str_code').values('str_code').aggregate(Sum('inv_d_sale'))
        totalsaleNov2 = InvoiceDaily.objects.filter(str_code__str_loc=getloc, str_code__str_city=getCity, str_code__str_name=getStore, prd_code = prdcode, inv_d_date__gte=dt.date(int(year),11,24), inv_d_date__lte=dt.date(int(year),12,7)).select_related('prd_code','str_code').values('str_code').aggregate(Sum('inv_d_sale'))
        totalsaleDec  = InvoiceDaily.objects.filter(str_code__str_loc=getloc, str_code__str_city=getCity, str_code__str_name=getStore, prd_code = prdcode, inv_d_date__gte=dt.date(int(year),12,8), inv_d_date__lte=dt.date(int(year),12,21)).select_related('prd_code','str_code').values('str_code').aggregate(Sum('inv_d_sale'))
        totalsaleDec2 = InvoiceDaily.objects.filter(str_code__str_loc=getloc, str_code__str_city=getCity, str_code__str_name=getStore, prd_code = prdcode, inv_d_date__gte=dt.date(int(year),12,22), inv_d_date__lte=dt.date(int(year)+1,1,4)).select_related('prd_code','str_code').values('str_code').aggregate(Sum('inv_d_sale'))
            
    else:
        # 데이터
        data = InvoiceMonthly.objects.filter(prd_code = prdcode, inv_m_date__year=year).select_related('prd_code','str_code').values('str_code','str_code__str_city','str_code__str_name','prd_code__prd_name').annotate(Sum('inv_m_sale'))
        
        
        # 월/일자 리스트 (38개)
        px_month = [12, 12,  1, 1,  2,  2, 2,  3, 3,  3,  4,  4,  4, 5,  5,  5, 6,  6,  6, 7,  7, 7,  8,  8,   8, 9, 9,   9, 10, 10, 10, 11, 11, 11, 12, 12, 12, 1]
        px_date  = [31, 29, 12, 31, 2, 16, 28, 2, 16, 31, 6, 20, 30, 4, 18, 31, 1, 15, 30, 6, 20, 31, 10, 24, 31, 7, 21, 30,  5, 19, 31,  2, 23, 30, 7,  21, 31, 4]
        
        for i in range(0,25):
            saleData = list(InvoiceDaily.objects.filter(prd_code = prdcode, inv_d_date__year=int(year)-1, inv_d_date__month=px_month[i], inv_d_date__day=px_date[i]).select_related('prd_code','str_code').values('str_code').annotate(Sum('inv_d_sale')).values_list('inv_d_sale__sum', flat=True))
        
        
        
        
        saleData1231 = list(InvoiceDaily.objects.filter(prd_code = prdcode, inv_d_date__year=int(year)-1, inv_d_date__month=12, inv_d_date__day=31).select_related('prd_code','str_code').values('str_code').annotate(Sum('inv_d_sale')).values_list('inv_d_sale__sum', flat=True))
        saleData1229 = list(InvoiceDaily.objects.filter(prd_code = prdcode, inv_d_date__year=int(year)-1, inv_d_date__month=12, inv_d_date__day=29).select_related('prd_code','str_code').values('str_code').annotate(Sum('inv_d_sale')).values_list('inv_d_sale__sum', flat=True))
        saleData0112 = list(InvoiceDaily.objects.filter(prd_code = prdcode, inv_d_date__year=int(year), inv_d_date__month=1, inv_d_date__day=12).select_related('prd_code','str_code').values('str_code').annotate(Sum('inv_d_sale')).values_list('inv_d_sale__sum', flat=True))
        saleData0131 = list(InvoiceDaily.objects.filter(prd_code = prdcode, inv_d_date__year=int(year), inv_d_date__month=1, inv_d_date__day=31).select_related('prd_code','str_code').values('str_code').annotate(Sum('inv_d_sale')).values_list('inv_d_sale__sum', flat=True))
        saleData0202 = list(InvoiceDaily.objects.filter(prd_code = prdcode, inv_d_date__year=int(year), inv_d_date__month=2, inv_d_date__day=2).select_related('prd_code','str_code').values('str_code').annotate(Sum('inv_d_sale')).values_list('inv_d_sale__sum', flat=True))
        saleData0216 = list(InvoiceDaily.objects.filter(prd_code = prdcode, inv_d_date__year=int(year), inv_d_date__month=2, inv_d_date__day=16).select_related('prd_code','str_code').values('str_code').annotate(Sum('inv_d_sale')).values_list('inv_d_sale__sum', flat=True))
        saleData0228 = list(InvoiceDaily.objects.filter(prd_code = prdcode, inv_d_date__year=int(year), inv_d_date__month=2, inv_d_date__day=28).select_related('prd_code','str_code').values('str_code').annotate(Sum('inv_d_sale')).values_list('inv_d_sale__sum', flat=True))
        saleData0302 = list(InvoiceDaily.objects.filter(prd_code = prdcode, inv_d_date__year=int(year), inv_d_date__month=3, inv_d_date__day=2).select_related('prd_code','str_code').values('str_code').annotate(Sum('inv_d_sale')).values_list('inv_d_sale__sum', flat=True))
        saleData0316 = list(InvoiceDaily.objects.filter(prd_code = prdcode, inv_d_date__year=int(year), inv_d_date__month=3, inv_d_date__day=16).select_related('prd_code','str_code').values('str_code').annotate(Sum('inv_d_sale')).values_list('inv_d_sale__sum', flat=True))
        saleData0331 = list(InvoiceDaily.objects.filter(prd_code = prdcode, inv_d_date__year=int(year), inv_d_date__month=3, inv_d_date__day=31).select_related('prd_code','str_code').values('str_code').annotate(Sum('inv_d_sale')).values_list('inv_d_sale__sum', flat=True))
        saleData0406 = list(InvoiceDaily.objects.filter(prd_code = prdcode, inv_d_date__year=int(year), inv_d_date__month=4, inv_d_date__day=6).select_related('prd_code','str_code').values('str_code').annotate(Sum('inv_d_sale')).values_list('inv_d_sale__sum', flat=True))
        
        # 12/30-1/12
        saleJan_ = [j-k for j,k in zip(saleData1231,saleData1229)]
        [l+m for l,m in zip(saleJan_,saleData0112)]    
        saleJan = saleJan_ + saleData0112
        # 1/13-2/2
        saleJan2_ = [j-k for j,k in zip(saleData0131,saleData0112)]
        [l+m for l,m in zip(saleJan2_,saleData0202)]
        saleJan2 = saleJan2_ + saleData0202
        # 2/3-2/16
        saleFeb = [j-k for j,k in zip(saleData0216,saleData0202)]
        # 2/17-3/2
        saleFeb2_ = [j-k for j,k in zip(saleData0228,saleData0216)]
        [l+m for l,m in zip(saleFeb2_,saleData0302)]
        saleFeb2 = saleFeb2_ + saleData0302
        # 3/3-3/16
        saleMar = [j-k for j,k in zip(saleData0316,saleData0302)]
        # 3/17-4/6
        saleMar2_ = [j-k for j,k in zip(saleData0331,saleData0316)]
        [l+m for l,m in zip(saleMar2_,saleData0406)]
        saleMar2 = saleMar2_ + saleData0406
        
        for i in range(0, 25):
            # 월/일자 리스트 (24개)
            px_month = [12, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, 11, 11, 11, 11, 12, 12, 12, 12, 1]
            px_date = [30, 12, 13, 2, 3, 16, 17, 2, 3, 16, 17, 6, 7, 20, 21, 4, 5, 18, 19, 1, 2, 15, 16, 6, 7, 20, 21, 10, 11, 24, 25, 7, 8, 21, 22, 5, 6, 19, 20, 2, 3, 23, 24, 7, 8, 21, 22, 4]
            # 1-1월
            saleData0 = list(InvoiceDaily.objects.filter(prd_code = prdcode, inv_d_date__year=int(year)-1, inv_d_date__month=px_month[i], inv_d_date__day=px_date[i]).select_related('prd_code','str_code').values('str_code').annotate(Sum('inv_d_sale')).values_list('inv_d_sale__sum', flat=True))
            saleData1 = list(InvoiceDaily.objects.filter(prd_code = prdcode, inv_d_date__year=year, inv_d_date__month=px_month[i+1], inv_d_date__day=px_date[i+1]).select_related('prd_code','str_code').values('str_code').annotate(Sum('inv_d_sale')).values_list('inv_d_sale__sum', flat=True))
            # 1-2~12-1월
            saleData2 = list(InvoiceDaily.objects.filter(prd_code = prdcode, inv_d_date__year=year, inv_d_date__month=px_month[2*i-2], inv_d_date__day=px_date[2*i-2]).select_related('prd_code','str_code').values('str_code').annotate(Sum('inv_d_sale')).values_list('inv_d_sale__sum', flat=True))
            saleData3 = list(InvoiceDaily.objects.filter(prd_code = prdcode, inv_d_date__year=year, inv_d_date__month=px_month[2*i-1], inv_d_date__day=px_date[2*i-1]).select_related('prd_code','str_code').values('str_code').annotate(Sum('inv_d_sale')).values_list('inv_d_sale__sum', flat=True))
            saleData4 = list(InvoiceDaily.objects.filter(prd_code = prdcode, inv_d_date__year=year, inv_d_date__month=px_month[2*i-3], inv_d_date__day=px_date[2*i-3]).select_related('prd_code','str_code').values('str_code').annotate(Sum('inv_d_sale')).values_list('inv_d_sale__sum', flat=True))
            #12-2월
            saleData32 = list(InvoiceDaily.objects.filter(prd_code = prdcode, inv_d_date__year=int(year)+1, inv_d_date__month=px_month[2*i-1], inv_d_date__day=px_date[2*i-1]).select_related('prd_code','str_code').values('str_code').annotate(Sum('inv_d_sale')).values_list('inv_d_sale__sum', flat=True))
            
            
            # saleJan,saleJan2,saleFeb,saleFeb2,saleMar,saleMar2,saleApr,saleApr2,saleMay,saleMay2,saleJun,saleJun2 = [],[],[],[],[],[],[],[],[],[],[],[]
            # saleJul,saleJul2,saleAug,saleAug2,saleSep,saleSep2,saleOct,saleOct2,saleNov,saleNov2,saleDec,saleDec2 = [],[],[],[],[],[],[],[],[],[],[],[]
            
            # (1-1)월
                
                
            if i > 1:
                # (1-2)~(12-1)월                
                [l+m for l,m in zip(saleData2,saleData3)]    
                saledataSum3 = saleData2 + saleData3                        
                saledataSum4 = [n-o for n,o in zip(saledataSum3,saleData4)] 
                # (12-2)월
                [p-q for p,q in zip(saleData2,saleData32)]
                saledataSum2 = saleData2 + saleData32
                saledataSum5 = [r-s for r,s in zip(saledataSum2,saleData4)] 
                
                
                # if i == 2:
                #     saleJan2 = saledataSum4
                # if i == 3:
                #     saleFeb  = saledataSum4
                # if i == 4:
                #     saleFeb2 = saledataSum4
                if i == 5:
                    saleMar  = saledataSum4
                if i == 6:
                    saleMar2 = saledataSum4
                if i == 7:
                    saleApr  = saledataSum4
                if i == 8:
                    saleApr2 = saledataSum4
                if i == 9:
                    saleMay  = saledataSum4
                if i == 10:
                    saleMay2 = saledataSum4
                if i == 11:
                    saleJun  = saledataSum4
                if i == 12:
                    saleJun2 = saledataSum4
                if i == 13:
                    saleJul  = saledataSum4
                if i == 14:
                    saleJul2 = saledataSum4
                if i == 15:
                    saleAug  = saledataSum4
                if i == 16:
                    saleAug2 = saledataSum4
                if i == 17:
                    saleSep  = saledataSum4
                if i == 18:
                    saleSep2 = saledataSum4
                if i == 19:
                    saleOct  = saledataSum4
                if i == 20:
                    saleOct2 = saledataSum4
                if i == 21:
                    saleNov  = saledataSum4
                if i == 22:
                    saleNov2 = saledataSum4
                if i == 23:
                    saleDec  = saledataSum4
                if i == 24:
                    saleDec2 = saledataSum5
            
        
        # 월별 판매 총합 데이터
        totalsaleJan  = sum(saleJan)
        totalsaleJan2 = sum(saleJan2)
        totalsaleFeb  = sum(saleFeb)
        totalsaleFeb2 = sum(saleFeb2)
        totalsaleMar  = sum(saleMar)
        totalsaleMar2 = sum(saleMar2)
        totalsaleApr  = sum(saleApr)
        totalsaleApr2 = sum(saleApr2)
        totalsaleMay  = sum(saleMay)
        totalsaleMay2 = sum(saleMay2)
        totalsaleJun  = sum(saleJun)
        totalsaleJun2 = sum(saleJun2)
        totalsaleJul  = sum(saleJul)
        totalsaleJul2 = sum(saleJul2)
        totalsaleAug  = sum(saleAug)
        totalsaleAug2 = sum(saleAug2)
        totalsaleSep  = sum(saleSep)
        totalsaleSep2 = sum(saleSep2)
        totalsaleOct  = sum(saleOct)
        totalsaleOct2 = sum(saleOct2)
        totalsaleNov  = sum(saleNov)
        totalsaleNov2 = sum(saleNov2)
        totalsaleDec  = sum(saleDec)
        totalsaleDec2 = sum(saleDec2)
        # 최상단 총합계 데이터
        totaldata = totalsaleJan + totalsaleJan2 + totalsaleFeb + totalsaleFeb2 + totalsaleMar + totalsaleMar2 + totalsaleApr + totalsaleApr2 + totalsaleMay + totalsaleMay2 + totalsaleJun + totalsaleJun2 + totalsaleJul + totalsaleJul2 + totalsaleAug + totalsaleAug2 + totalsaleSep + totalsaleSep2 + totalsaleOct + totalsaleOct2 + totalsaleNov + totalsaleNov2 + totalsaleDec + totalsaleDec2
    
    context = {'product':product, 'yearDate':year, 'data':data, 'prdcode':prdcode, 'prdname':prdname, 'totaldata':totaldata,
               'saleJan':saleJan, 'saleFeb':saleFeb, 'saleMar':saleMar, 'saleApr':saleApr, 'saleMay':saleMay, 'saleJun':saleJun, 
               'saleJul':saleJul, 'saleAug':saleAug, 'saleSep':saleSep, 'saleOct':saleOct, 'saleNov':saleNov, 'saleDec':saleDec, 
               'saleJan2':saleJan2, 'saleFeb2':saleFeb2, 'saleMar2':saleMar2, 'saleApr2':saleApr2, 'saleMay2':saleMay2, 'saleJun2':saleJun2, 
               'saleJul2':saleJul2, 'saleAug2':saleAug2, 'saleSep2':saleSep2, 'saleOct2':saleOct2, 'saleNov2':saleNov2, 'saleDec2':saleDec2,
               'totalsaleJan':totalsaleJan, 'totalsaleFeb':totalsaleFeb, 'totalsaleMar':totalsaleMar, 'totalsaleApr':totalsaleApr,
               'totalsaleMay':totalsaleMay, 'totalsaleJun':totalsaleJun, 'totalsaleJul':totalsaleJul, 'totalsaleAug':totalsaleAug, 
               'totalsaleSep':totalsaleSep, 'totalsaleOct':totalsaleOct, 'totalsaleNov':totalsaleNov, 'totalsaleDec':totalsaleDec,
               'totalsaleJan2':totalsaleJan2, 'totalsaleFeb2':totalsaleFeb2, 'totalsaleMar2':totalsaleMar2, 'totalsaleApr2':totalsaleApr2,
               'totalsaleMay2':totalsaleMay2, 'totalsaleJun2':totalsaleJun2, 'totalsaleJul2':totalsaleJul2, 'totalsaleAug2':totalsaleAug2, 
               'totalsaleSep2':totalsaleSep2, 'totalsaleOct2':totalsaleOct2, 'totalsaleNov2':totalsaleNov2, 'totalsaleDec2':totalsaleDec2,
               'loc':loc, 'city':city, 'str':str}

    return render(request, 'csp/index.html', context)

# Add Field Select Box
def select(request):
    # get select box value
    getloc = request.GET.get('location')
    
    # set select box value
    city = Store.objects.filter(str_loc=getloc).values('str_city').distinct().order_by('str_city')
    
    return JsonResponse({'data': list(city)})

def select2(request):
    # get select box value
    getCity = request.GET.get('city')
    
    # set select box value
    store = Store.objects.filter(str_city=getCity).values('str_name','str_code').order_by('str_name')
    
    return JsonResponse({'data': list(store)})