from django.shortcuts import render, redirect
from django.db.models import Sum
from csd.models import InvoiceDaily, Product
from datetime import datetime

# Create your views here.
def index(request):
    # html에서 선택한 날짜 받아오기
    try:
        year = request.GET.get('input-year')   #2022
    except TypeError:
        year = datetime.today().year
    
    # html에서 선택한 select box value 받아오기
    prdcode = request.GET.get('input-prd')  #상품코드
    
    # 상단에 표시할 상품명
    prdname = Product.objects.filter(prd_code = prdcode).values_list('prd_name', flat=True)
    # 데이터
    data = InvoiceDaily.objects.filter(prd_code = prdcode, inv_d_date__year=year).select_related('prd_code','str_code').values('str_code','str_code__str_city','str_code__str_name','prd_code__prd_name').annotate(Sum('inv_d_save'),Sum('inv_d_buy'),Sum('inv_d_return'),Sum('inv_d_sale'),Sum('inv_d_stock'))
    # 월별 판매 데이터
    saleJan = list(InvoiceDaily.objects.filter(prd_code = prdcode, inv_d_date__year=year,inv_d_date__month=1).select_related('prd_code','str_code').values('str_code').annotate(Sum('inv_d_sale')))
    saleFeb = list(InvoiceDaily.objects.filter(prd_code = prdcode, inv_d_date__year=year,inv_d_date__month=2).select_related('prd_code','str_code').values('str_code').annotate(Sum('inv_d_sale')))
    saleMar = list(InvoiceDaily.objects.filter(prd_code = prdcode, inv_d_date__year=year,inv_d_date__month=3).select_related('prd_code','str_code').values('str_code').annotate(Sum('inv_d_sale')))
    saleApr = list(InvoiceDaily.objects.filter(prd_code = prdcode, inv_d_date__year=year,inv_d_date__month=4).select_related('prd_code','str_code').values('str_code').annotate(Sum('inv_d_sale')))
    saleMay = list(InvoiceDaily.objects.filter(prd_code = prdcode, inv_d_date__year=year,inv_d_date__month=5).select_related('prd_code','str_code').values('str_code').annotate(Sum('inv_d_sale')))
    saleJun = list(InvoiceDaily.objects.filter(prd_code = prdcode, inv_d_date__year=year,inv_d_date__month=6).select_related('prd_code','str_code').values('str_code').annotate(Sum('inv_d_sale')))
    saleJul = list(InvoiceDaily.objects.filter(prd_code = prdcode, inv_d_date__year=year,inv_d_date__month=7).select_related('prd_code','str_code').values('str_code').annotate(Sum('inv_d_sale')))
    saleAug = list(InvoiceDaily.objects.filter(prd_code = prdcode, inv_d_date__year=year,inv_d_date__month=8).select_related('prd_code','str_code').values('str_code').annotate(Sum('inv_d_sale')))
    saleSep = list(InvoiceDaily.objects.filter(prd_code = prdcode, inv_d_date__year=year,inv_d_date__month=9).select_related('prd_code','str_code').values('str_code').annotate(Sum('inv_d_sale')))
    saleOct = list(InvoiceDaily.objects.filter(prd_code = prdcode, inv_d_date__year=year,inv_d_date__month=10).select_related('prd_code','str_code').values('str_code').annotate(Sum('inv_d_sale')))
    saleNov = list(InvoiceDaily.objects.filter(prd_code = prdcode, inv_d_date__year=year,inv_d_date__month=11).select_related('prd_code','str_code').values('str_code').annotate(Sum('inv_d_sale')))
    saleDec = list(InvoiceDaily.objects.filter(prd_code = prdcode, inv_d_date__year=year,inv_d_date__month=12).select_related('prd_code','str_code').values('str_code').annotate(Sum('inv_d_sale')))
    # 최하단 총합계 데이터
    totaldata = InvoiceDaily.objects.filter(prd_code = prdcode, inv_d_date__year=year).select_related('prd_code','str_code').aggregate(Sum('inv_d_save'),Sum('inv_d_buy'),Sum('inv_d_return'),Sum('inv_d_sale'),Sum('inv_d_stock'))
    # 월별 판매 총합 데이터
    totalsaleJan = InvoiceDaily.objects.filter(prd_code = prdcode, inv_d_date__year=year, inv_d_date__month=1).select_related('prd_code','str_code').values('str_code').aggregate(Sum('inv_d_sale'))
    totalsaleFeb = InvoiceDaily.objects.filter(prd_code = prdcode, inv_d_date__year=year, inv_d_date__month=2).select_related('prd_code','str_code').values('str_code').aggregate(Sum('inv_d_sale'))
    totalsaleMar = InvoiceDaily.objects.filter(prd_code = prdcode, inv_d_date__year=year, inv_d_date__month=3).select_related('prd_code','str_code').values('str_code').aggregate(Sum('inv_d_sale'))
    totalsaleApr = InvoiceDaily.objects.filter(prd_code = prdcode, inv_d_date__year=year, inv_d_date__month=4).select_related('prd_code','str_code').values('str_code').aggregate(Sum('inv_d_sale'))
    totalsaleMay = InvoiceDaily.objects.filter(prd_code = prdcode, inv_d_date__year=year, inv_d_date__month=5).select_related('prd_code','str_code').values('str_code').aggregate(Sum('inv_d_sale'))
    totalsaleJun = InvoiceDaily.objects.filter(prd_code = prdcode, inv_d_date__year=year, inv_d_date__month=6).select_related('prd_code','str_code').values('str_code').aggregate(Sum('inv_d_sale'))
    totalsaleJul = InvoiceDaily.objects.filter(prd_code = prdcode, inv_d_date__year=year, inv_d_date__month=7).select_related('prd_code','str_code').values('str_code').aggregate(Sum('inv_d_sale'))
    totalsaleAug = InvoiceDaily.objects.filter(prd_code = prdcode, inv_d_date__year=year, inv_d_date__month=8).select_related('prd_code','str_code').values('str_code').aggregate(Sum('inv_d_sale'))
    totalsaleSep = InvoiceDaily.objects.filter(prd_code = prdcode, inv_d_date__year=year, inv_d_date__month=9).select_related('prd_code','str_code').values('str_code').aggregate(Sum('inv_d_sale'))
    totalsaleOct = InvoiceDaily.objects.filter(prd_code = prdcode, inv_d_date__year=year, inv_d_date__month=10).select_related('prd_code','str_code').values('str_code').aggregate(Sum('inv_d_sale'))
    totalsaleNov = InvoiceDaily.objects.filter(prd_code = prdcode, inv_d_date__year=year, inv_d_date__month=11).select_related('prd_code','str_code').values('str_code').aggregate(Sum('inv_d_sale'))
    totalsaleDec = InvoiceDaily.objects.filter(prd_code = prdcode, inv_d_date__year=year, inv_d_date__month=12).select_related('prd_code','str_code').values('str_code').aggregate(Sum('inv_d_sale'))

    context = {'yearDate':year, 'data':data, 'prdcode':prdcode, 'prdname':prdname, 'totaldata':totaldata, 
               'saleJan':saleJan, 'saleFeb':saleFeb, 'saleMar':saleMar, 'saleApr':saleApr, 'saleMay':saleMay, 'saleJun':saleJun, 
               'saleJul':saleJul, 'saleAug':saleAug, 'saleSep':saleSep, 'saleOct':saleOct, 'saleNov':saleNov, 'saleDec':saleDec,
               'totalsaleJan':totalsaleJan, 'totalsaleFeb':totalsaleFeb, 'totalsaleMar':totalsaleMar, 'totalsaleApr':totalsaleApr,
               'totalsaleMay':totalsaleMay, 'totalsaleJun':totalsaleJun, 'totalsaleJul':totalsaleJul, 'totalsaleAug':totalsaleAug, 
               'totalsaleSep':totalsaleSep, 'totalsaleOct':totalsaleOct, 'totalsaleNov':totalsaleNov, 'totalsaleDec':totalsaleDec}
    
    return render(request, 'csy/index.html', context)