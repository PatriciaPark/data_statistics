from django.shortcuts import render
from django.db.models import Sum
from csd.models import InvoiceDaily, Product
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
        
    # 상단에 표시할 상품명
    prdname = Product.objects.filter(prd_code = prdcode).values_list('prd_name', flat=True)
    # 데이터
    data = InvoiceDaily.objects.filter(prd_code = prdcode, inv_d_date__year=year).select_related('prd_code','str_code').values('str_code','str_code__str_city','str_code__str_name','prd_code__prd_name').annotate(Sum('inv_d_sale'))
    # 월별 판매 데이터
    saleJan  = list(InvoiceDaily.objects.filter(prd_code = prdcode, inv_d_date__gte=dt.date(int(year)-1,12,30), inv_d_date__lte=dt.date(int(year),1,12)).select_related('prd_code','str_code').values('str_code').annotate(Sum('inv_d_sale')))
    saleJan2 = list(InvoiceDaily.objects.filter(prd_code = prdcode, inv_d_date__gte=dt.date(int(year),1,13), inv_d_date__lte=dt.date(int(year),2,2)).select_related('prd_code','str_code').values('str_code').annotate(Sum('inv_d_sale')))
    saleFeb  = list(InvoiceDaily.objects.filter(prd_code = prdcode, inv_d_date__gte=dt.date(int(year),2,3), inv_d_date__lte=dt.date(int(year),2,16)).select_related('prd_code','str_code').values('str_code').annotate(Sum('inv_d_sale')))
    saleFeb2 = list(InvoiceDaily.objects.filter(prd_code = prdcode, inv_d_date__gte=dt.date(int(year),2,17), inv_d_date__lte=dt.date(int(year),3,2)).select_related('prd_code','str_code').values('str_code').annotate(Sum('inv_d_sale')))
    saleMar  = list(InvoiceDaily.objects.filter(prd_code = prdcode, inv_d_date__gte=dt.date(int(year),3,3), inv_d_date__lte=dt.date(int(year),3,16)).select_related('prd_code','str_code').values('str_code').annotate(Sum('inv_d_sale')))
    saleMar2 = list(InvoiceDaily.objects.filter(prd_code = prdcode, inv_d_date__gte=dt.date(int(year),3,17), inv_d_date__lte=dt.date(int(year),4,6)).select_related('prd_code','str_code').values('str_code').annotate(Sum('inv_d_sale')))
    saleApr  = list(InvoiceDaily.objects.filter(prd_code = prdcode, inv_d_date__gte=dt.date(int(year),4,7), inv_d_date__lte=dt.date(int(year),4,20)).select_related('prd_code','str_code').values('str_code').annotate(Sum('inv_d_sale')))
    saleApr2 = list(InvoiceDaily.objects.filter(prd_code = prdcode, inv_d_date__gte=dt.date(int(year),4,21), inv_d_date__lte=dt.date(int(year),5,4)).select_related('prd_code','str_code').values('str_code').annotate(Sum('inv_d_sale')))
    saleMay  = list(InvoiceDaily.objects.filter(prd_code = prdcode, inv_d_date__gte=dt.date(int(year),5,5), inv_d_date__lte=dt.date(int(year),5,18)).select_related('prd_code','str_code').values('str_code').annotate(Sum('inv_d_sale')))
    saleMay2 = list(InvoiceDaily.objects.filter(prd_code = prdcode, inv_d_date__gte=dt.date(int(year),5,19), inv_d_date__lte=dt.date(int(year),6,1)).select_related('prd_code','str_code').values('str_code').annotate(Sum('inv_d_sale')))
    saleJun  = list(InvoiceDaily.objects.filter(prd_code = prdcode, inv_d_date__gte=dt.date(int(year),6,2), inv_d_date__lte=dt.date(int(year),6,15)).select_related('prd_code','str_code').values('str_code').annotate(Sum('inv_d_sale')))
    saleJun2 = list(InvoiceDaily.objects.filter(prd_code = prdcode, inv_d_date__gte=dt.date(int(year),6,16), inv_d_date__lte=dt.date(int(year),7,6)).select_related('prd_code','str_code').values('str_code').annotate(Sum('inv_d_sale')))
    saleJul  = list(InvoiceDaily.objects.filter(prd_code = prdcode, inv_d_date__gte=dt.date(int(year),7,7), inv_d_date__lte=dt.date(int(year),7,20)).select_related('prd_code','str_code').values('str_code').annotate(Sum('inv_d_sale')))
    saleJul2 = list(InvoiceDaily.objects.filter(prd_code = prdcode, inv_d_date__gte=dt.date(int(year),7,21), inv_d_date__lte=dt.date(int(year),8,10)).select_related('prd_code','str_code').values('str_code').annotate(Sum('inv_d_sale')))
    saleAug  = list(InvoiceDaily.objects.filter(prd_code = prdcode, inv_d_date__gte=dt.date(int(year),8,11), inv_d_date__lte=dt.date(int(year),8,24)).select_related('prd_code','str_code').values('str_code').annotate(Sum('inv_d_sale')))
    saleAug2 = list(InvoiceDaily.objects.filter(prd_code = prdcode, inv_d_date__gte=dt.date(int(year),8,25), inv_d_date__lte=dt.date(int(year),9,7)).select_related('prd_code','str_code').values('str_code').annotate(Sum('inv_d_sale')))
    saleSep  = list(InvoiceDaily.objects.filter(prd_code = prdcode, inv_d_date__gte=dt.date(int(year),9,8), inv_d_date__lte=dt.date(int(year),9,21)).select_related('prd_code','str_code').values('str_code').annotate(Sum('inv_d_sale')))
    saleSep2 = list(InvoiceDaily.objects.filter(prd_code = prdcode, inv_d_date__gte=dt.date(int(year),9,22), inv_d_date__lte=dt.date(int(year),10,5)).select_related('prd_code','str_code').values('str_code').annotate(Sum('inv_d_sale')))
    saleOct  = list(InvoiceDaily.objects.filter(prd_code = prdcode, inv_d_date__gte=dt.date(int(year),10,6), inv_d_date__lte=dt.date(int(year),10,19)).select_related('prd_code','str_code').values('str_code').annotate(Sum('inv_d_sale')))
    saleOct2 = list(InvoiceDaily.objects.filter(prd_code = prdcode, inv_d_date__gte=dt.date(int(year),10,20), inv_d_date__lte=dt.date(int(year),11,2)).select_related('prd_code','str_code').values('str_code').annotate(Sum('inv_d_sale')))
    saleNov  = list(InvoiceDaily.objects.filter(prd_code = prdcode, inv_d_date__gte=dt.date(int(year),11,3), inv_d_date__lte=dt.date(int(year),11,23)).select_related('prd_code','str_code').values('str_code').annotate(Sum('inv_d_sale')))
    saleNov2 = list(InvoiceDaily.objects.filter(prd_code = prdcode, inv_d_date__gte=dt.date(int(year),11,24), inv_d_date__lte=dt.date(int(year),12,7)).select_related('prd_code','str_code').values('str_code').annotate(Sum('inv_d_sale')))
    saleDec  = list(InvoiceDaily.objects.filter(prd_code = prdcode, inv_d_date__gte=dt.date(int(year),12,8), inv_d_date__lte=dt.date(int(year),12,21)).select_related('prd_code','str_code').values('str_code').annotate(Sum('inv_d_sale')))
    saleDec2 = list(InvoiceDaily.objects.filter(prd_code = prdcode, inv_d_date__gte=dt.date(int(year),12,22), inv_d_date__lte=dt.date(int(year)+1,1,4)).select_related('prd_code','str_code').values('str_code').annotate(Sum('inv_d_sale')))
    # 최하단 총합계 데이터
    totaldata = InvoiceDaily.objects.filter(prd_code = prdcode, inv_d_date__year=year).select_related('prd_code','str_code').aggregate(Sum('inv_d_sale'))
    # 월별 판매 총합 데이터
    totalsaleJan  = InvoiceDaily.objects.filter(prd_code = prdcode, inv_d_date__gte=dt.date(int(year)-1,12,30), inv_d_date__lte=dt.date(int(year),1,12)).select_related('prd_code','str_code').values('str_code').aggregate(Sum('inv_d_sale'))
    totalsaleJan2 = InvoiceDaily.objects.filter(prd_code = prdcode, inv_d_date__gte=dt.date(int(year),1,13), inv_d_date__lte=dt.date(int(year),2,2)).select_related('prd_code','str_code').values('str_code').aggregate(Sum('inv_d_sale'))
    totalsaleFeb  = InvoiceDaily.objects.filter(prd_code = prdcode, inv_d_date__gte=dt.date(int(year),2,3), inv_d_date__lte=dt.date(int(year),2,16)).select_related('prd_code','str_code').values('str_code').aggregate(Sum('inv_d_sale'))
    totalsaleFeb2 = InvoiceDaily.objects.filter(prd_code = prdcode, inv_d_date__gte=dt.date(int(year),2,17), inv_d_date__lte=dt.date(int(year),3,2)).select_related('prd_code','str_code').values('str_code').aggregate(Sum('inv_d_sale'))
    totalsaleMar  = InvoiceDaily.objects.filter(prd_code = prdcode, inv_d_date__gte=dt.date(int(year),3,3), inv_d_date__lte=dt.date(int(year),3,16)).select_related('prd_code','str_code').values('str_code').aggregate(Sum('inv_d_sale'))
    totalsaleMar2 = InvoiceDaily.objects.filter(prd_code = prdcode, inv_d_date__gte=dt.date(int(year),3,17), inv_d_date__lte=dt.date(int(year),4,6)).select_related('prd_code','str_code').values('str_code').aggregate(Sum('inv_d_sale'))
    totalsaleApr  = InvoiceDaily.objects.filter(prd_code = prdcode, inv_d_date__gte=dt.date(int(year),4,7), inv_d_date__lte=dt.date(int(year),4,20)).select_related('prd_code','str_code').values('str_code').aggregate(Sum('inv_d_sale'))
    totalsaleApr2 = InvoiceDaily.objects.filter(prd_code = prdcode, inv_d_date__gte=dt.date(int(year),4,21), inv_d_date__lte=dt.date(int(year),5,4)).select_related('prd_code','str_code').values('str_code').aggregate(Sum('inv_d_sale'))
    totalsaleMay  = InvoiceDaily.objects.filter(prd_code = prdcode, inv_d_date__gte=dt.date(int(year),5,5), inv_d_date__lte=dt.date(int(year),5,18)).select_related('prd_code','str_code').values('str_code').aggregate(Sum('inv_d_sale'))
    totalsaleMay2 = InvoiceDaily.objects.filter(prd_code = prdcode, inv_d_date__gte=dt.date(int(year),5,19), inv_d_date__lte=dt.date(int(year),6,1)).select_related('prd_code','str_code').values('str_code').aggregate(Sum('inv_d_sale'))
    totalsaleJun  = InvoiceDaily.objects.filter(prd_code = prdcode, inv_d_date__gte=dt.date(int(year),6,2), inv_d_date__lte=dt.date(int(year),6,15)).select_related('prd_code','str_code').values('str_code').aggregate(Sum('inv_d_sale'))
    totalsaleJun2 = InvoiceDaily.objects.filter(prd_code = prdcode, inv_d_date__gte=dt.date(int(year),6,16), inv_d_date__lte=dt.date(int(year),7,6)).select_related('prd_code','str_code').values('str_code').aggregate(Sum('inv_d_sale'))
    totalsaleJul  = InvoiceDaily.objects.filter(prd_code = prdcode, inv_d_date__gte=dt.date(int(year),7,7), inv_d_date__lte=dt.date(int(year),7,20)).select_related('prd_code','str_code').values('str_code').aggregate(Sum('inv_d_sale'))
    totalsaleJul2 = InvoiceDaily.objects.filter(prd_code = prdcode, inv_d_date__gte=dt.date(int(year),7,21), inv_d_date__lte=dt.date(int(year),8,10)).select_related('prd_code','str_code').values('str_code').aggregate(Sum('inv_d_sale'))
    totalsaleAug  = InvoiceDaily.objects.filter(prd_code = prdcode, inv_d_date__gte=dt.date(int(year),8,11), inv_d_date__lte=dt.date(int(year),8,24)).select_related('prd_code','str_code').values('str_code').aggregate(Sum('inv_d_sale'))
    totalsaleAug2 = InvoiceDaily.objects.filter(prd_code = prdcode, inv_d_date__gte=dt.date(int(year),8,25), inv_d_date__lte=dt.date(int(year),9,7)).select_related('prd_code','str_code').values('str_code').aggregate(Sum('inv_d_sale'))
    totalsaleSep  = InvoiceDaily.objects.filter(prd_code = prdcode, inv_d_date__gte=dt.date(int(year),9,8), inv_d_date__lte=dt.date(int(year),9,21)).select_related('prd_code','str_code').values('str_code').aggregate(Sum('inv_d_sale'))
    totalsaleSep2 = InvoiceDaily.objects.filter(prd_code = prdcode, inv_d_date__gte=dt.date(int(year),9,22), inv_d_date__lte=dt.date(int(year),10,5)).select_related('prd_code','str_code').values('str_code').aggregate(Sum('inv_d_sale'))
    totalsaleOct  = InvoiceDaily.objects.filter(prd_code = prdcode, inv_d_date__gte=dt.date(int(year),10,6), inv_d_date__lte=dt.date(int(year),10,19)).select_related('prd_code','str_code').values('str_code').aggregate(Sum('inv_d_sale'))
    totalsaleOct2 = InvoiceDaily.objects.filter(prd_code = prdcode, inv_d_date__gte=dt.date(int(year),10,20), inv_d_date__lte=dt.date(int(year),11,1)).select_related('prd_code','str_code').values('str_code').aggregate(Sum('inv_d_sale'))
    totalsaleNov  = InvoiceDaily.objects.filter(prd_code = prdcode, inv_d_date__gte=dt.date(int(year),11,3), inv_d_date__lte=dt.date(int(year),11,23)).select_related('prd_code','str_code').values('str_code').aggregate(Sum('inv_d_sale'))
    totalsaleNov2 = InvoiceDaily.objects.filter(prd_code = prdcode, inv_d_date__gte=dt.date(int(year),11,24), inv_d_date__lte=dt.date(int(year),12,7)).select_related('prd_code','str_code').values('str_code').aggregate(Sum('inv_d_sale'))
    totalsaleDec  = InvoiceDaily.objects.filter(prd_code = prdcode, inv_d_date__gte=dt.date(int(year),12,8), inv_d_date__lte=dt.date(int(year),12,21)).select_related('prd_code','str_code').values('str_code').aggregate(Sum('inv_d_sale'))
    totalsaleDec2 = InvoiceDaily.objects.filter(prd_code = prdcode, inv_d_date__gte=dt.date(int(year),12,22), inv_d_date__lte=dt.date(int(year)+1,1,4)).select_related('prd_code','str_code').values('str_code').aggregate(Sum('inv_d_sale'))
        
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
               'totalsaleSep2':totalsaleSep2, 'totalsaleOct2':totalsaleOct2, 'totalsaleNov2':totalsaleNov2, 'totalsaleDec2':totalsaleDec2}

    return render(request, 'csp/index.html', context)