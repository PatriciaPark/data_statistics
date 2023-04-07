from django.shortcuts import render
from django.http import JsonResponse
from django.db.models import Sum, Max
from csd.models import InvoiceMonthly, InvoiceDaily, Product, Store
from datetime import datetime
from django.db import connection
import calendar

# Create your views here.
def index(request):
    # html에서 선택한 날짜 받아오기
    year = request.GET.get('input-year')   #2022
    if year is None:
        year = datetime.today().year
    
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
    
    # select box list
    product = Product.objects.all()
    
    # 상단에 표시할 상품명
    prdname = Product.objects.filter(prd_code = prdcode).values_list('prd_name', flat=True)
    
    # template로 전송
    context = {'product':product, 'yearDate':year, 'prdcode':prdcode, 'prdname':prdname, 'loc':loc, 'city':city, 'str':str}
    
    # read data
    data, totaldata = [], []
        
    # 지역만 선택
    if getloc != 'all' and (getCity is None or getCity == 'all') and (getStore is None or getStore == 'all'):
        # 데이터
        data = InvoiceMonthly.objects.filter(str_code__str_loc=getloc, prd_code = prdcode, inv_m_date__year=year).select_related('prd_code','str_code').values('str_code','str_code__str_city','str_code__str_name','prd_code__prd_name').annotate(Sum('inv_m_save'),Sum('inv_m_buy'),Sum('inv_m_return'),Sum('inv_m_sale'),Sum('inv_m_stock'))
        # 최상단 총합계 데이터
        totaldata = InvoiceMonthly.objects.filter(str_code__str_loc=getloc, prd_code = prdcode, inv_m_date__year=year).select_related('prd_code','str_code').aggregate(Sum('inv_m_save'),Sum('inv_m_buy'),Sum('inv_m_return'),Sum('inv_m_sale'),Sum('inv_m_stock'))
    # 지역 및 시까지 선택
    elif getloc != 'all' and getCity is not None and (getStore is None or getStore == 'all'):
        # 데이터
        data = InvoiceMonthly.objects.filter(str_code__str_loc=getloc, str_code__str_city=getCity, prd_code = prdcode, inv_m_date__year=year).select_related('prd_code','str_code').values('str_code','str_code__str_city','str_code__str_name','prd_code__prd_name').annotate(Sum('inv_m_save'),Sum('inv_m_buy'),Sum('inv_m_return'),Sum('inv_m_sale'),Sum('inv_m_stock'))
        # 최상단 총합계 데이터
        totaldata = InvoiceMonthly.objects.filter(str_code__str_loc=getloc, str_code__str_city=getCity, prd_code = prdcode, inv_m_date__year=year).select_related('prd_code','str_code').aggregate(Sum('inv_m_save'),Sum('inv_m_buy'),Sum('inv_m_return'),Sum('inv_m_sale'),Sum('inv_m_stock'))
    #지역, 시, 매장 선택
    elif getloc != 'all' and getCity is not None and getStore is not None:
        # 데이터
        data = InvoiceMonthly.objects.filter(str_code__str_loc=getloc, str_code__str_city=getCity, str_code__str_name=getStore, prd_code = prdcode, inv_m_date__year=year).select_related('prd_code','str_code').values('str_code','str_code__str_city','str_code__str_name','prd_code__prd_name').annotate(Sum('inv_m_save'),Sum('inv_m_buy'),Sum('inv_m_return'),Sum('inv_m_sale'),Sum('inv_m_stock'))
        # 최상단 총합계 데이터
        totaldata = InvoiceMonthly.objects.filter(str_code__str_loc=getloc, str_code__str_city=getCity, str_code__str_name=getStore, prd_code = prdcode, inv_m_date__year=year).select_related('prd_code','str_code').aggregate(Sum('inv_m_save'),Sum('inv_m_buy'),Sum('inv_m_return'),Sum('inv_m_sale'),Sum('inv_m_stock'))
    else:
        # 데이터
        data = InvoiceMonthly.objects.filter(prd_code = prdcode, inv_m_date__year=year).select_related('prd_code','str_code').values('str_code','str_code__str_city','str_code__str_name','prd_code__prd_name').annotate(Sum('inv_m_save'),Sum('inv_m_buy'),Sum('inv_m_return'),Sum('inv_m_sale'),Sum('inv_m_stock'))
        # 최상단 총합계 데이터
        totaldata = InvoiceMonthly.objects.filter(prd_code = prdcode, inv_m_date__year=year).select_related('prd_code','str_code').aggregate(Sum('inv_m_save'),Sum('inv_m_buy'),Sum('inv_m_return'),Sum('inv_m_sale'),Sum('inv_m_stock')) 
        
    context.update({'data':data, 'totaldata':totaldata})
    
    return render(request, 'csy/index.html', context)

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

def details(request):
    # html에서 선택한 날짜 받아오기
    year = request.GET.get('input-year')   #2022
    if year is None:
        year = datetime.today().year
    
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
    
    # select box list
    product = Product.objects.all()
    
    # 상단에 표시할 상품명
    prdname = Product.objects.filter(prd_code = prdcode).values_list('prd_name', flat=True)
    
    # template로 전송
    context = {'product':product, 'yearDate':year, 'prdcode':prdcode, 'prdname':prdname, 'loc':loc, 'city':city, 'str':str}
    
    # read data
    data, totaldata = [], []
        
    # 지역만 선택
    if getloc != 'all' and (getCity is None or getCity == 'all') and (getStore is None or getStore == 'all'):
        # 데이터
        data = InvoiceMonthly.objects.filter(str_code__str_loc=getloc, prd_code = prdcode, inv_m_date__year=year).select_related('prd_code','str_code').values('str_code','str_code__str_city','str_code__str_name','prd_code__prd_name').annotate(Sum('inv_m_save'),Sum('inv_m_buy'),Sum('inv_m_return'),Sum('inv_m_sale'),Sum('inv_m_stock'))
        # 최상단 총합계 데이터
        totaldata = InvoiceMonthly.objects.filter(str_code__str_loc=getloc, prd_code = prdcode, inv_m_date__year=year).select_related('prd_code','str_code').aggregate(Sum('inv_m_save'),Sum('inv_m_buy'),Sum('inv_m_return'),Sum('inv_m_sale'),Sum('inv_m_stock'))
        # 월별 판매 데이터
        saleJan = list(InvoiceMonthly.objects.filter(str_code__str_loc=getloc, prd_code = prdcode, inv_m_date__year=year, inv_m_date__month=1).select_related('prd_code','str_code').values('str_code','str_code__str_city','str_code__str_name','prd_code__prd_name').annotate(Sum('inv_m_sale')))
        saleFeb = list(InvoiceMonthly.objects.filter(str_code__str_loc=getloc, prd_code = prdcode, inv_m_date__year=year, inv_m_date__month=2).select_related('prd_code','str_code').values('str_code','str_code__str_city','str_code__str_name','prd_code__prd_name').annotate(Sum('inv_m_sale')))
        saleMar = list(InvoiceMonthly.objects.filter(str_code__str_loc=getloc, prd_code = prdcode, inv_m_date__year=year, inv_m_date__month=3).select_related('prd_code','str_code').values('str_code','str_code__str_city','str_code__str_name','prd_code__prd_name').annotate(Sum('inv_m_sale')))
        saleApr = list(InvoiceMonthly.objects.filter(str_code__str_loc=getloc, prd_code = prdcode, inv_m_date__year=year, inv_m_date__month=4).select_related('prd_code','str_code').values('str_code','str_code__str_city','str_code__str_name','prd_code__prd_name').annotate(Sum('inv_m_sale')))
        saleMay = list(InvoiceMonthly.objects.filter(str_code__str_loc=getloc, prd_code = prdcode, inv_m_date__year=year, inv_m_date__month=5).select_related('prd_code','str_code').values('str_code','str_code__str_city','str_code__str_name','prd_code__prd_name').annotate(Sum('inv_m_sale')))
        saleJun = list(InvoiceMonthly.objects.filter(str_code__str_loc=getloc, prd_code = prdcode, inv_m_date__year=year, inv_m_date__month=6).select_related('prd_code','str_code').values('str_code','str_code__str_city','str_code__str_name','prd_code__prd_name').annotate(Sum('inv_m_sale')))
        saleJul = list(InvoiceMonthly.objects.filter(str_code__str_loc=getloc, prd_code = prdcode, inv_m_date__year=year, inv_m_date__month=7).select_related('prd_code','str_code').values('str_code','str_code__str_city','str_code__str_name','prd_code__prd_name').annotate(Sum('inv_m_sale')))
        saleAug = list(InvoiceMonthly.objects.filter(str_code__str_loc=getloc, prd_code = prdcode, inv_m_date__year=year, inv_m_date__month=8).select_related('prd_code','str_code').values('str_code','str_code__str_city','str_code__str_name','prd_code__prd_name').annotate(Sum('inv_m_sale')))
        saleSep = list(InvoiceMonthly.objects.filter(str_code__str_loc=getloc, prd_code = prdcode, inv_m_date__year=year, inv_m_date__month=9).select_related('prd_code','str_code').values('str_code','str_code__str_city','str_code__str_name','prd_code__prd_name').annotate(Sum('inv_m_sale')))
        saleOct = list(InvoiceMonthly.objects.filter(str_code__str_loc=getloc, prd_code = prdcode, inv_m_date__year=year, inv_m_date__month=10).select_related('prd_code','str_code').values('str_code','str_code__str_city','str_code__str_name','prd_code__prd_name').annotate(Sum('inv_m_sale')))
        saleNov = list(InvoiceMonthly.objects.filter(str_code__str_loc=getloc, prd_code = prdcode, inv_m_date__year=year, inv_m_date__month=11).select_related('prd_code','str_code').values('str_code','str_code__str_city','str_code__str_name','prd_code__prd_name').annotate(Sum('inv_m_sale')))
        saleDec = list(InvoiceMonthly.objects.filter(str_code__str_loc=getloc, prd_code = prdcode, inv_m_date__year=year, inv_m_date__month=12).select_related('prd_code','str_code').values('str_code','str_code__str_city','str_code__str_name','prd_code__prd_name').annotate(Sum('inv_m_sale')))
        # 월별 판매 총합 데이터
        totalsaleJan = InvoiceMonthly.objects.filter(str_code__str_loc=getloc, prd_code = prdcode, inv_m_date__year=year, inv_m_date__month=1).select_related('prd_code','str_code').values('str_code').aggregate(Sum('inv_m_sale'))
        totalsaleFeb = InvoiceMonthly.objects.filter(str_code__str_loc=getloc, prd_code = prdcode, inv_m_date__year=year, inv_m_date__month=2).select_related('prd_code','str_code').values('str_code').aggregate(Sum('inv_m_sale'))
        totalsaleMar = InvoiceMonthly.objects.filter(str_code__str_loc=getloc, prd_code = prdcode, inv_m_date__year=year, inv_m_date__month=3).select_related('prd_code','str_code').values('str_code').aggregate(Sum('inv_m_sale'))
        totalsaleApr = InvoiceMonthly.objects.filter(str_code__str_loc=getloc, prd_code = prdcode, inv_m_date__year=year, inv_m_date__month=4).select_related('prd_code','str_code').values('str_code').aggregate(Sum('inv_m_sale'))
        totalsaleMay = InvoiceMonthly.objects.filter(str_code__str_loc=getloc, prd_code = prdcode, inv_m_date__year=year, inv_m_date__month=5).select_related('prd_code','str_code').values('str_code').aggregate(Sum('inv_m_sale'))
        totalsaleJun = InvoiceMonthly.objects.filter(str_code__str_loc=getloc, prd_code = prdcode, inv_m_date__year=year, inv_m_date__month=6).select_related('prd_code','str_code').values('str_code').aggregate(Sum('inv_m_sale'))
        totalsaleJul = InvoiceMonthly.objects.filter(str_code__str_loc=getloc, prd_code = prdcode, inv_m_date__year=year, inv_m_date__month=7).select_related('prd_code','str_code').values('str_code').aggregate(Sum('inv_m_sale'))
        totalsaleAug = InvoiceMonthly.objects.filter(str_code__str_loc=getloc, prd_code = prdcode, inv_m_date__year=year, inv_m_date__month=8).select_related('prd_code','str_code').values('str_code').aggregate(Sum('inv_m_sale'))
        totalsaleSep = InvoiceMonthly.objects.filter(str_code__str_loc=getloc, prd_code = prdcode, inv_m_date__year=year, inv_m_date__month=9).select_related('prd_code','str_code').values('str_code').aggregate(Sum('inv_m_sale'))
        totalsaleOct = InvoiceMonthly.objects.filter(str_code__str_loc=getloc, prd_code = prdcode, inv_m_date__year=year, inv_m_date__month=10).select_related('prd_code','str_code').values('str_code').aggregate(Sum('inv_m_sale'))
        totalsaleNov = InvoiceMonthly.objects.filter(str_code__str_loc=getloc, prd_code = prdcode, inv_m_date__year=year, inv_m_date__month=11).select_related('prd_code','str_code').values('str_code').aggregate(Sum('inv_m_sale'))
        totalsaleDec = InvoiceMonthly.objects.filter(str_code__str_loc=getloc, prd_code = prdcode, inv_m_date__year=year, inv_m_date__month=12).select_related('prd_code','str_code').values('str_code').aggregate(Sum('inv_m_sale'))
        
    
    # 지역 및 시까지 선택
    elif getloc != 'all' and getCity is not None and (getStore is None or getStore == 'all'):
        # 데이터
        data = InvoiceMonthly.objects.filter(str_code__str_loc=getloc, str_code__str_city=getCity, prd_code = prdcode, inv_m_date__year=year).select_related('prd_code','str_code').values('str_code','str_code__str_city','str_code__str_name','prd_code__prd_name').annotate(Sum('inv_m_save'),Sum('inv_m_buy'),Sum('inv_m_return'),Sum('inv_m_sale'),Sum('inv_m_stock'))
        # 최상단 총합계 데이터
        totaldata = InvoiceMonthly.objects.filter(str_code__str_loc=getloc, str_code__str_city=getCity, prd_code = prdcode, inv_m_date__year=year).select_related('prd_code','str_code').aggregate(Sum('inv_m_save'),Sum('inv_m_buy'),Sum('inv_m_return'),Sum('inv_m_sale'),Sum('inv_m_stock'))
        # 월별 판매 데이터
        saleJan = list(InvoiceMonthly.objects.filter(str_code__str_loc=getloc, str_code__str_city=getCity, prd_code = prdcode, inv_m_date__year=year, inv_m_date__month=1).select_related('prd_code','str_code').values('str_code','str_code__str_city','str_code__str_name','prd_code__prd_name').annotate(Sum('inv_m_sale')))
        saleFeb = list(InvoiceMonthly.objects.filter(str_code__str_loc=getloc, str_code__str_city=getCity, prd_code = prdcode, inv_m_date__year=year, inv_m_date__month=2).select_related('prd_code','str_code').values('str_code','str_code__str_city','str_code__str_name','prd_code__prd_name').annotate(Sum('inv_m_sale')))
        saleMar = list(InvoiceMonthly.objects.filter(str_code__str_loc=getloc, str_code__str_city=getCity, prd_code = prdcode, inv_m_date__year=year, inv_m_date__month=3).select_related('prd_code','str_code').values('str_code','str_code__str_city','str_code__str_name','prd_code__prd_name').annotate(Sum('inv_m_sale')))
        saleApr = list(InvoiceMonthly.objects.filter(str_code__str_loc=getloc, str_code__str_city=getCity, prd_code = prdcode, inv_m_date__year=year, inv_m_date__month=4).select_related('prd_code','str_code').values('str_code','str_code__str_city','str_code__str_name','prd_code__prd_name').annotate(Sum('inv_m_sale')))
        saleMay = list(InvoiceMonthly.objects.filter(str_code__str_loc=getloc, str_code__str_city=getCity, prd_code = prdcode, inv_m_date__year=year, inv_m_date__month=5).select_related('prd_code','str_code').values('str_code','str_code__str_city','str_code__str_name','prd_code__prd_name').annotate(Sum('inv_m_sale')))
        saleJun = list(InvoiceMonthly.objects.filter(str_code__str_loc=getloc, str_code__str_city=getCity, prd_code = prdcode, inv_m_date__year=year, inv_m_date__month=6).select_related('prd_code','str_code').values('str_code','str_code__str_city','str_code__str_name','prd_code__prd_name').annotate(Sum('inv_m_sale')))
        saleJul = list(InvoiceMonthly.objects.filter(str_code__str_loc=getloc, str_code__str_city=getCity, prd_code = prdcode, inv_m_date__year=year, inv_m_date__month=7).select_related('prd_code','str_code').values('str_code','str_code__str_city','str_code__str_name','prd_code__prd_name').annotate(Sum('inv_m_sale')))
        saleAug = list(InvoiceMonthly.objects.filter(str_code__str_loc=getloc, str_code__str_city=getCity, prd_code = prdcode, inv_m_date__year=year, inv_m_date__month=8).select_related('prd_code','str_code').values('str_code','str_code__str_city','str_code__str_name','prd_code__prd_name').annotate(Sum('inv_m_sale')))
        saleSep = list(InvoiceMonthly.objects.filter(str_code__str_loc=getloc, str_code__str_city=getCity, prd_code = prdcode, inv_m_date__year=year, inv_m_date__month=9).select_related('prd_code','str_code').values('str_code','str_code__str_city','str_code__str_name','prd_code__prd_name').annotate(Sum('inv_m_sale')))
        saleOct = list(InvoiceMonthly.objects.filter(str_code__str_loc=getloc, str_code__str_city=getCity, prd_code = prdcode, inv_m_date__year=year, inv_m_date__month=10).select_related('prd_code','str_code').values('str_code','str_code__str_city','str_code__str_name','prd_code__prd_name').annotate(Sum('inv_m_sale')))
        saleNov = list(InvoiceMonthly.objects.filter(str_code__str_loc=getloc, str_code__str_city=getCity, prd_code = prdcode, inv_m_date__year=year, inv_m_date__month=11).select_related('prd_code','str_code').values('str_code','str_code__str_city','str_code__str_name','prd_code__prd_name').annotate(Sum('inv_m_sale')))
        saleDec = list(InvoiceMonthly.objects.filter(str_code__str_loc=getloc, str_code__str_city=getCity, prd_code = prdcode, inv_m_date__year=year, inv_m_date__month=12).select_related('prd_code','str_code').values('str_code','str_code__str_city','str_code__str_name','prd_code__prd_name').annotate(Sum('inv_m_sale')))
        # 월별 판매 총합 데이터
        totalsaleJan = InvoiceMonthly.objects.filter(str_code__str_loc=getloc, str_code__str_city=getCity, prd_code = prdcode, inv_m_date__year=year, inv_m_date__month=1).select_related('prd_code','str_code').values('str_code').aggregate(Sum('inv_m_sale'))
        totalsaleFeb = InvoiceMonthly.objects.filter(str_code__str_loc=getloc, str_code__str_city=getCity, prd_code = prdcode, inv_m_date__year=year, inv_m_date__month=2).select_related('prd_code','str_code').values('str_code').aggregate(Sum('inv_m_sale'))
        totalsaleMar = InvoiceMonthly.objects.filter(str_code__str_loc=getloc, str_code__str_city=getCity, prd_code = prdcode, inv_m_date__year=year, inv_m_date__month=3).select_related('prd_code','str_code').values('str_code').aggregate(Sum('inv_m_sale'))
        totalsaleApr = InvoiceMonthly.objects.filter(str_code__str_loc=getloc, str_code__str_city=getCity, prd_code = prdcode, inv_m_date__year=year, inv_m_date__month=4).select_related('prd_code','str_code').values('str_code').aggregate(Sum('inv_m_sale'))
        totalsaleMay = InvoiceMonthly.objects.filter(str_code__str_loc=getloc, str_code__str_city=getCity, prd_code = prdcode, inv_m_date__year=year, inv_m_date__month=5).select_related('prd_code','str_code').values('str_code').aggregate(Sum('inv_m_sale'))
        totalsaleJun = InvoiceMonthly.objects.filter(str_code__str_loc=getloc, str_code__str_city=getCity, prd_code = prdcode, inv_m_date__year=year, inv_m_date__month=6).select_related('prd_code','str_code').values('str_code').aggregate(Sum('inv_m_sale'))
        totalsaleJul = InvoiceMonthly.objects.filter(str_code__str_loc=getloc, str_code__str_city=getCity, prd_code = prdcode, inv_m_date__year=year, inv_m_date__month=7).select_related('prd_code','str_code').values('str_code').aggregate(Sum('inv_m_sale'))
        totalsaleAug = InvoiceMonthly.objects.filter(str_code__str_loc=getloc, str_code__str_city=getCity, prd_code = prdcode, inv_m_date__year=year, inv_m_date__month=8).select_related('prd_code','str_code').values('str_code').aggregate(Sum('inv_m_sale'))
        totalsaleSep = InvoiceMonthly.objects.filter(str_code__str_loc=getloc, str_code__str_city=getCity, prd_code = prdcode, inv_m_date__year=year, inv_m_date__month=9).select_related('prd_code','str_code').values('str_code').aggregate(Sum('inv_m_sale'))
        totalsaleOct = InvoiceMonthly.objects.filter(str_code__str_loc=getloc, str_code__str_city=getCity, prd_code = prdcode, inv_m_date__year=year, inv_m_date__month=10).select_related('prd_code','str_code').values('str_code').aggregate(Sum('inv_m_sale'))
        totalsaleNov = InvoiceMonthly.objects.filter(str_code__str_loc=getloc, str_code__str_city=getCity, prd_code = prdcode, inv_m_date__year=year, inv_m_date__month=11).select_related('prd_code','str_code').values('str_code').aggregate(Sum('inv_m_sale'))
        totalsaleDec = InvoiceMonthly.objects.filter(str_code__str_loc=getloc, str_code__str_city=getCity, prd_code = prdcode, inv_m_date__year=year, inv_m_date__month=12).select_related('prd_code','str_code').values('str_code').aggregate(Sum('inv_m_sale'))
    
    #지역, 시, 매장 선택
    elif getloc != 'all' and getCity is not None and getStore is not None:
        # 데이터
        data = InvoiceMonthly.objects.filter(str_code__str_loc=getloc, str_code__str_city=getCity, str_code__str_name=getStore, prd_code = prdcode, inv_m_date__year=year).select_related('prd_code','str_code').values('str_code','str_code__str_city','str_code__str_name','prd_code__prd_name').annotate(Sum('inv_m_save'),Sum('inv_m_buy'),Sum('inv_m_return'),Sum('inv_m_sale'),Sum('inv_m_stock'))
        # 최상단 총합계 데이터
        totaldata = InvoiceMonthly.objects.filter(str_code__str_loc=getloc, str_code__str_city=getCity, str_code__str_name=getStore, prd_code = prdcode, inv_m_date__year=year).select_related('prd_code','str_code').aggregate(Sum('inv_m_save'),Sum('inv_m_buy'),Sum('inv_m_return'),Sum('inv_m_sale'),Sum('inv_m_stock'))
        # 월별 판매 데이터
        saleJan = list(InvoiceMonthly.objects.filter(str_code__str_loc=getloc, str_code__str_city=getCity, str_code__str_name=getStore, prd_code = prdcode, inv_m_date__year=year, inv_m_date__month=1).select_related('prd_code','str_code').values('str_code','str_code__str_city','str_code__str_name','prd_code__prd_name').annotate(Sum('inv_m_sale')))
        saleFeb = list(InvoiceMonthly.objects.filter(str_code__str_loc=getloc, str_code__str_city=getCity, str_code__str_name=getStore, prd_code = prdcode, inv_m_date__year=year, inv_m_date__month=2).select_related('prd_code','str_code').values('str_code','str_code__str_city','str_code__str_name','prd_code__prd_name').annotate(Sum('inv_m_sale')))
        saleMar = list(InvoiceMonthly.objects.filter(str_code__str_loc=getloc, str_code__str_city=getCity, str_code__str_name=getStore, prd_code = prdcode, inv_m_date__year=year, inv_m_date__month=3).select_related('prd_code','str_code').values('str_code','str_code__str_city','str_code__str_name','prd_code__prd_name').annotate(Sum('inv_m_sale')))
        saleApr = list(InvoiceMonthly.objects.filter(str_code__str_loc=getloc, str_code__str_city=getCity, str_code__str_name=getStore, prd_code = prdcode, inv_m_date__year=year, inv_m_date__month=4).select_related('prd_code','str_code').values('str_code','str_code__str_city','str_code__str_name','prd_code__prd_name').annotate(Sum('inv_m_sale')))
        saleMay = list(InvoiceMonthly.objects.filter(str_code__str_loc=getloc, str_code__str_city=getCity, str_code__str_name=getStore, prd_code = prdcode, inv_m_date__year=year, inv_m_date__month=5).select_related('prd_code','str_code').values('str_code','str_code__str_city','str_code__str_name','prd_code__prd_name').annotate(Sum('inv_m_sale')))
        saleJun = list(InvoiceMonthly.objects.filter(str_code__str_loc=getloc, str_code__str_city=getCity, str_code__str_name=getStore, prd_code = prdcode, inv_m_date__year=year, inv_m_date__month=6).select_related('prd_code','str_code').values('str_code','str_code__str_city','str_code__str_name','prd_code__prd_name').annotate(Sum('inv_m_sale')))
        saleJul = list(InvoiceMonthly.objects.filter(str_code__str_loc=getloc, str_code__str_city=getCity, str_code__str_name=getStore, prd_code = prdcode, inv_m_date__year=year, inv_m_date__month=7).select_related('prd_code','str_code').values('str_code','str_code__str_city','str_code__str_name','prd_code__prd_name').annotate(Sum('inv_m_sale')))
        saleAug = list(InvoiceMonthly.objects.filter(str_code__str_loc=getloc, str_code__str_city=getCity, str_code__str_name=getStore, prd_code = prdcode, inv_m_date__year=year, inv_m_date__month=8).select_related('prd_code','str_code').values('str_code','str_code__str_city','str_code__str_name','prd_code__prd_name').annotate(Sum('inv_m_sale')))
        saleSep = list(InvoiceMonthly.objects.filter(str_code__str_loc=getloc, str_code__str_city=getCity, str_code__str_name=getStore, prd_code = prdcode, inv_m_date__year=year, inv_m_date__month=9).select_related('prd_code','str_code').values('str_code','str_code__str_city','str_code__str_name','prd_code__prd_name').annotate(Sum('inv_m_sale')))
        saleOct = list(InvoiceMonthly.objects.filter(str_code__str_loc=getloc, str_code__str_city=getCity, str_code__str_name=getStore, prd_code = prdcode, inv_m_date__year=year, inv_m_date__month=10).select_related('prd_code','str_code').values('str_code','str_code__str_city','str_code__str_name','prd_code__prd_name').annotate(Sum('inv_m_sale')))
        saleNov = list(InvoiceMonthly.objects.filter(str_code__str_loc=getloc, str_code__str_city=getCity, str_code__str_name=getStore, prd_code = prdcode, inv_m_date__year=year, inv_m_date__month=11).select_related('prd_code','str_code').values('str_code','str_code__str_city','str_code__str_name','prd_code__prd_name').annotate(Sum('inv_m_sale')))
        saleDec = list(InvoiceMonthly.objects.filter(str_code__str_loc=getloc, str_code__str_city=getCity, str_code__str_name=getStore, prd_code = prdcode, inv_m_date__year=year, inv_m_date__month=12).select_related('prd_code','str_code').values('str_code','str_code__str_city','str_code__str_name','prd_code__prd_name').annotate(Sum('inv_m_sale')))
        # 월별 판매 총합 데이터
        totalsaleJan = InvoiceMonthly.objects.filter(str_code__str_loc=getloc, str_code__str_city=getCity, str_code__str_name=getStore, prd_code = prdcode, inv_m_date__year=year, inv_m_date__month=1).select_related('prd_code','str_code').values('str_code').aggregate(Sum('inv_m_sale'))
        totalsaleFeb = InvoiceMonthly.objects.filter(str_code__str_loc=getloc, str_code__str_city=getCity, str_code__str_name=getStore, prd_code = prdcode, inv_m_date__year=year, inv_m_date__month=2).select_related('prd_code','str_code').values('str_code').aggregate(Sum('inv_m_sale'))
        totalsaleMar = InvoiceMonthly.objects.filter(str_code__str_loc=getloc, str_code__str_city=getCity, str_code__str_name=getStore, prd_code = prdcode, inv_m_date__year=year, inv_m_date__month=3).select_related('prd_code','str_code').values('str_code').aggregate(Sum('inv_m_sale'))
        totalsaleApr = InvoiceMonthly.objects.filter(str_code__str_loc=getloc, str_code__str_city=getCity, str_code__str_name=getStore, prd_code = prdcode, inv_m_date__year=year, inv_m_date__month=4).select_related('prd_code','str_code').values('str_code').aggregate(Sum('inv_m_sale'))
        totalsaleMay = InvoiceMonthly.objects.filter(str_code__str_loc=getloc, str_code__str_city=getCity, str_code__str_name=getStore, prd_code = prdcode, inv_m_date__year=year, inv_m_date__month=5).select_related('prd_code','str_code').values('str_code').aggregate(Sum('inv_m_sale'))
        totalsaleJun = InvoiceMonthly.objects.filter(str_code__str_loc=getloc, str_code__str_city=getCity, str_code__str_name=getStore, prd_code = prdcode, inv_m_date__year=year, inv_m_date__month=6).select_related('prd_code','str_code').values('str_code').aggregate(Sum('inv_m_sale'))
        totalsaleJul = InvoiceMonthly.objects.filter(str_code__str_loc=getloc, str_code__str_city=getCity, str_code__str_name=getStore, prd_code = prdcode, inv_m_date__year=year, inv_m_date__month=7).select_related('prd_code','str_code').values('str_code').aggregate(Sum('inv_m_sale'))
        totalsaleAug = InvoiceMonthly.objects.filter(str_code__str_loc=getloc, str_code__str_city=getCity, str_code__str_name=getStore, prd_code = prdcode, inv_m_date__year=year, inv_m_date__month=8).select_related('prd_code','str_code').values('str_code').aggregate(Sum('inv_m_sale'))
        totalsaleSep = InvoiceMonthly.objects.filter(str_code__str_loc=getloc, str_code__str_city=getCity, str_code__str_name=getStore, prd_code = prdcode, inv_m_date__year=year, inv_m_date__month=9).select_related('prd_code','str_code').values('str_code').aggregate(Sum('inv_m_sale'))
        totalsaleOct = InvoiceMonthly.objects.filter(str_code__str_loc=getloc, str_code__str_city=getCity, str_code__str_name=getStore, prd_code = prdcode, inv_m_date__year=year, inv_m_date__month=10).select_related('prd_code','str_code').values('str_code').aggregate(Sum('inv_m_sale'))
        totalsaleNov = InvoiceMonthly.objects.filter(str_code__str_loc=getloc, str_code__str_city=getCity, str_code__str_name=getStore, prd_code = prdcode, inv_m_date__year=year, inv_m_date__month=11).select_related('prd_code','str_code').values('str_code').aggregate(Sum('inv_m_sale'))
        totalsaleDec = InvoiceMonthly.objects.filter(str_code__str_loc=getloc, str_code__str_city=getCity, str_code__str_name=getStore, prd_code = prdcode, inv_m_date__year=year, inv_m_date__month=12).select_related('prd_code','str_code').values('str_code').aggregate(Sum('inv_m_sale'))
    
    else:
        # 데이터
        data = InvoiceMonthly.objects.filter(prd_code = prdcode, inv_m_date__year=year).select_related('prd_code','str_code').values('str_code','str_code__str_city','str_code__str_name','prd_code__prd_name').annotate(Sum('inv_m_save'),Sum('inv_m_buy'),Sum('inv_m_return'),Sum('inv_m_sale'),Sum('inv_m_stock'))
        # 최상단 총합계 데이터
        totaldata = InvoiceMonthly.objects.filter(prd_code = prdcode, inv_m_date__year=year).select_related('prd_code','str_code').aggregate(Sum('inv_m_save'),Sum('inv_m_buy'),Sum('inv_m_return'),Sum('inv_m_sale'),Sum('inv_m_stock')) 
      
        # 월별 판매 데이터
        saleJan = list(InvoiceMonthly.objects.filter(prd_code = prdcode, inv_m_date__year=year, inv_m_date__month=1).select_related('prd_code','str_code').values('str_code','str_code__str_city','str_code__str_name','prd_code__prd_name').annotate(Sum('inv_m_sale')))
        saleFeb = list(InvoiceMonthly.objects.filter(prd_code = prdcode, inv_m_date__year=year, inv_m_date__month=2).select_related('prd_code','str_code').values('str_code','str_code__str_city','str_code__str_name','prd_code__prd_name').annotate(Sum('inv_m_sale')))
        saleMar = list(InvoiceMonthly.objects.filter(prd_code = prdcode, inv_m_date__year=year, inv_m_date__month=3).select_related('prd_code','str_code').values('str_code','str_code__str_city','str_code__str_name','prd_code__prd_name').annotate(Sum('inv_m_sale')))
        saleApr = list(InvoiceMonthly.objects.filter(prd_code = prdcode, inv_m_date__year=year, inv_m_date__month=4).select_related('prd_code','str_code').values('str_code','str_code__str_city','str_code__str_name','prd_code__prd_name').annotate(Sum('inv_m_sale')))
        saleMay = list(InvoiceMonthly.objects.filter(prd_code = prdcode, inv_m_date__year=year, inv_m_date__month=5).select_related('prd_code','str_code').values('str_code','str_code__str_city','str_code__str_name','prd_code__prd_name').annotate(Sum('inv_m_sale')))
        saleJun = list(InvoiceMonthly.objects.filter(prd_code = prdcode, inv_m_date__year=year, inv_m_date__month=6).select_related('prd_code','str_code').values('str_code','str_code__str_city','str_code__str_name','prd_code__prd_name').annotate(Sum('inv_m_sale')))
        saleJul = list(InvoiceMonthly.objects.filter(prd_code = prdcode, inv_m_date__year=year, inv_m_date__month=7).select_related('prd_code','str_code').values('str_code','str_code__str_city','str_code__str_name','prd_code__prd_name').annotate(Sum('inv_m_sale')))
        saleAug = list(InvoiceMonthly.objects.filter(prd_code = prdcode, inv_m_date__year=year, inv_m_date__month=8).select_related('prd_code','str_code').values('str_code','str_code__str_city','str_code__str_name','prd_code__prd_name').annotate(Sum('inv_m_sale')))
        saleSep = list(InvoiceMonthly.objects.filter(prd_code = prdcode, inv_m_date__year=year, inv_m_date__month=9).select_related('prd_code','str_code').values('str_code','str_code__str_city','str_code__str_name','prd_code__prd_name').annotate(Sum('inv_m_sale')))
        saleOct = list(InvoiceMonthly.objects.filter(prd_code = prdcode, inv_m_date__year=year, inv_m_date__month=10).select_related('prd_code','str_code').values('str_code','str_code__str_city','str_code__str_name','prd_code__prd_name').annotate(Sum('inv_m_sale')))
        saleNov = list(InvoiceMonthly.objects.filter(prd_code = prdcode, inv_m_date__year=year, inv_m_date__month=11).select_related('prd_code','str_code').values('str_code','str_code__str_city','str_code__str_name','prd_code__prd_name').annotate(Sum('inv_m_sale')))
        saleDec = list(InvoiceMonthly.objects.filter(prd_code = prdcode, inv_m_date__year=year, inv_m_date__month=12).select_related('prd_code','str_code').values('str_code','str_code__str_city','str_code__str_name','prd_code__prd_name').annotate(Sum('inv_m_sale')))
        # 월별 판매 총합 데이터
        totalsaleJan = InvoiceMonthly.objects.filter(prd_code = prdcode, inv_m_date__year=year, inv_m_date__month=1).select_related('prd_code','str_code').values('str_code').aggregate(Sum('inv_m_sale'))
        totalsaleFeb = InvoiceMonthly.objects.filter(prd_code = prdcode, inv_m_date__year=year, inv_m_date__month=2).select_related('prd_code','str_code').values('str_code').aggregate(Sum('inv_m_sale'))
        totalsaleMar = InvoiceMonthly.objects.filter(prd_code = prdcode, inv_m_date__year=year, inv_m_date__month=3).select_related('prd_code','str_code').values('str_code').aggregate(Sum('inv_m_sale'))
        totalsaleApr = InvoiceMonthly.objects.filter(prd_code = prdcode, inv_m_date__year=year, inv_m_date__month=4).select_related('prd_code','str_code').values('str_code').aggregate(Sum('inv_m_sale'))
        totalsaleMay = InvoiceMonthly.objects.filter(prd_code = prdcode, inv_m_date__year=year, inv_m_date__month=5).select_related('prd_code','str_code').values('str_code').aggregate(Sum('inv_m_sale'))
        totalsaleJun = InvoiceMonthly.objects.filter(prd_code = prdcode, inv_m_date__year=year, inv_m_date__month=6).select_related('prd_code','str_code').values('str_code').aggregate(Sum('inv_m_sale'))
        totalsaleJul = InvoiceMonthly.objects.filter(prd_code = prdcode, inv_m_date__year=year, inv_m_date__month=7).select_related('prd_code','str_code').values('str_code').aggregate(Sum('inv_m_sale'))
        totalsaleAug = InvoiceMonthly.objects.filter(prd_code = prdcode, inv_m_date__year=year, inv_m_date__month=8).select_related('prd_code','str_code').values('str_code').aggregate(Sum('inv_m_sale'))
        totalsaleSep = InvoiceMonthly.objects.filter(prd_code = prdcode, inv_m_date__year=year, inv_m_date__month=9).select_related('prd_code','str_code').values('str_code').aggregate(Sum('inv_m_sale'))
        totalsaleOct = InvoiceMonthly.objects.filter(prd_code = prdcode, inv_m_date__year=year, inv_m_date__month=10).select_related('prd_code','str_code').values('str_code').aggregate(Sum('inv_m_sale'))
        totalsaleNov = InvoiceMonthly.objects.filter(prd_code = prdcode, inv_m_date__year=year, inv_m_date__month=11).select_related('prd_code','str_code').values('str_code').aggregate(Sum('inv_m_sale'))
        totalsaleDec = InvoiceMonthly.objects.filter(prd_code = prdcode, inv_m_date__year=year, inv_m_date__month=12).select_related('prd_code','str_code').values('str_code').aggregate(Sum('inv_m_sale'))
    
    context.update({'data':data, 'totaldata':totaldata})
    context.update({'saleJan':saleJan, 'saleFeb':saleFeb, 'saleMar':saleMar, 'saleApr':saleApr, 'saleMay':saleMay, 'saleJun':saleJun, 
                    'saleJul':saleJul, 'saleAug':saleAug, 'saleSep':saleSep, 'saleOct':saleOct, 'saleNov':saleNov, 'saleDec':saleDec,
                    'totalsaleJan':totalsaleJan, 'totalsaleFeb':totalsaleFeb, 'totalsaleMar':totalsaleMar, 'totalsaleApr':totalsaleApr,
                    'totalsaleMay':totalsaleMay, 'totalsaleJun':totalsaleJun, 'totalsaleJul':totalsaleJul, 'totalsaleAug':totalsaleAug, 
                    'totalsaleSep':totalsaleSep, 'totalsaleOct':totalsaleOct, 'totalsaleNov':totalsaleNov, 'totalsaleDec':totalsaleDec
                    })
    
    return render(request, 'csy/salesDetail.html', context)