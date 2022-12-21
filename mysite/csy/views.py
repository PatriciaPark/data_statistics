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
    saleMon = InvoiceDaily.objects.filter(prd_code = prdcode, inv_d_date__year=year).select_related('prd_code','str_code').values('str_code','inv_d_date__month').annotate(Sum('inv_d_sale'))
    # 최하단 총합계 데이터
    totaldata = InvoiceDaily.objects.filter(prd_code = prdcode, inv_d_date__year=year).select_related('prd_code','str_code').aggregate(Sum('inv_d_save'),Sum('inv_d_buy'),Sum('inv_d_return'),Sum('inv_d_sale'),Sum('inv_d_stock'))
    totalsale = InvoiceDaily.objects.filter(prd_code = prdcode, inv_d_date__year=year).select_related('prd_code','str_code').values('inv_d_date__month').annotate(Sum('inv_d_sale'))
    
    print('saleMon',saleMon)
    print('totalsale',totalsale)
        
    context = {'yearDate':year, 'data':data, 'prdcode':prdcode, 'prdname':prdname, 'totaldata':totaldata, 'saleMon':saleMon, 'totalsale':totalsale}
    
    return render(request, 'csy/index.html', context)

def update(request):
    
    return redirect('/csy/?input-year=')