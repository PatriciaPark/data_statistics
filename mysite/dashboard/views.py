from django.shortcuts import render, redirect
from csd.models import *
from django.contrib import messages
from datetime import datetime
from .forms import Product_selling_priceForm
from django.http import HttpResponseRedirect
from .models import Dashboard_Table_month_basic
from csm.models import SumMonthly
from django.db.models import Sum

# Create your views here.
# index
def index(request):
    # html에서 선택한 연도도 받아오기
    
    try: 
        year = int(request.GET.get('input-year'))
    except:
        year = int(datetime.today().year)

    month = request.GET.get('input-month')
    if month is None:
        month = int(datetime.today().month)
    
    print(year, month)

    # 연간 전체 상품 판매량(라인차트)
    sumSale01 = SumMonthly.objects.filter(sum_m_date__year=year, sum_m_date__month=1).aggregate(Sum('sum_m_sale'))
    sumSale02 = SumMonthly.objects.filter(sum_m_date__year=year, sum_m_date__month=2).aggregate(Sum('sum_m_sale'))
    sumSale03 = SumMonthly.objects.filter(sum_m_date__year=year, sum_m_date__month=3).aggregate(Sum('sum_m_sale'))
    sumSale04 = SumMonthly.objects.filter(sum_m_date__year=year, sum_m_date__month=4).aggregate(Sum('sum_m_sale'))
    sumSale05 = SumMonthly.objects.filter(sum_m_date__year=year, sum_m_date__month=5).aggregate(Sum('sum_m_sale'))
    sumSale06 = SumMonthly.objects.filter(sum_m_date__year=year, sum_m_date__month=6).aggregate(Sum('sum_m_sale'))
    sumSale07 = SumMonthly.objects.filter(sum_m_date__year=year, sum_m_date__month=7).aggregate(Sum('sum_m_sale'))
    sumSale08 = SumMonthly.objects.filter(sum_m_date__year=year, sum_m_date__month=8).aggregate(Sum('sum_m_sale'))
    sumSale09 = SumMonthly.objects.filter(sum_m_date__year=year, sum_m_date__month=9).aggregate(Sum('sum_m_sale'))
    sumSale10 = SumMonthly.objects.filter(sum_m_date__year=year, sum_m_date__month=10).aggregate(Sum('sum_m_sale'))
    sumSale11 = SumMonthly.objects.filter(sum_m_date__year=year, sum_m_date__month=11).aggregate(Sum('sum_m_sale'))
    sumSale12 = SumMonthly.objects.filter(sum_m_date__year=year, sum_m_date__month=12).aggregate(Sum('sum_m_sale'))
    
    # 당해년도
    thisyear = datetime.today().year
    
    context = {'thisyear':thisyear, 'year':year, 'month':month, 'sumSale01':sumSale01, 'sumSale02':sumSale02, 'sumSale03':sumSale03, 'sumSale04':sumSale04, 'sumSale05':sumSale05, 'sumSale06':sumSale06, 
               'sumSale07':sumSale07, 'sumSale08':sumSale08, 'sumSale09':sumSale09, 'sumSale10':sumSale10, 'sumSale11':sumSale11, 'sumSale12':sumSale12}
    
    
    # 전체 판매량 제품 비율 (파이차트)
    sum11530035 = SumMonthly.objects.filter(prd_code = 11530035, sum_m_date__year=year).aggregate(Sum('sum_m_sale'))   #正官庄活蔘２８Ｄ高麗蔘活 / 力飲１００ｍｌ＊１０瓶
    sum11060162 = SumMonthly.objects.filter(prd_code = 11060162, sum_m_date__year=year).aggregate(Sum('sum_m_sale'))   #正官庄高麗蔘精ＥＶＥＲＹ / ＴＩＭＥ－秘１０ｍｌ＊２０入
    sum17010087 = SumMonthly.objects.filter(prd_code = 17010087, sum_m_date__year=year).aggregate(Sum('sum_m_sale'))   #預購正官庄活蔘２８Ｄ高麗 / 蔘活力飲禮盒１００ｍｌ＊８入
    sum17010088 = SumMonthly.objects.filter(prd_code = 17010088, sum_m_date__year=year).aggregate(Sum('sum_m_sale'))   #預購正官庄高麗蔘石榴飲 / ５０ｍｌ＊９入
    sum17010004 = SumMonthly.objects.filter(prd_code = 17010004, sum_m_date__year=year).aggregate(Sum('sum_m_sale'))   #預購正官庄高麗蔘野櫻莓飲
    sum17010002 = SumMonthly.objects.filter(prd_code = 17010002, sum_m_date__year=year).aggregate(Sum('sum_m_sale'))   #預購正官庄高麗蔘精ＥＶＥ / ＲＹＴＩＭＥ１０ｍｌ＊３０入
    # **제품이 추가될때마다 코드추가**    
    
    context.update({'sum11530035':sum11530035, 'sum11060162':sum11060162, 'sum17010087':sum17010087, 'sum17010088':sum17010088, 'sum17010004':sum17010004, 'sum17010002':sum17010002})
    
    # 월별 제품별 판매량 (바차트)
    sum11530035m = list(SumMonthly.objects.filter(prd_code = 11530035, sum_m_date__year=year, sum_m_date__month=month).aggregate(Sum('sum_m_sale')).values())[0]   #正官庄活蔘２８Ｄ高麗蔘活 / 力飲１００ｍｌ＊１０瓶
    sum11060162m = list(SumMonthly.objects.filter(prd_code = 11060162, sum_m_date__year=year, sum_m_date__month=month).aggregate(Sum('sum_m_sale')).values())[0]   #正官庄高麗蔘精ＥＶＥＲＹ / ＴＩＭＥ－秘１０ｍｌ＊２０入
    sum17010087m = list(SumMonthly.objects.filter(prd_code = 17010087, sum_m_date__year=year, sum_m_date__month=month).aggregate(Sum('sum_m_sale')).values())[0]   #預購正官庄活蔘２８Ｄ高麗 / 蔘活力飲禮盒１００ｍｌ＊８入
    sum17010088m = list(SumMonthly.objects.filter(prd_code = 17010088, sum_m_date__year=year, sum_m_date__month=month).aggregate(Sum('sum_m_sale')).values())[0]   #預購正官庄高麗蔘石榴飲 / ５０ｍｌ＊９入
    sum17010004m = list(SumMonthly.objects.filter(prd_code = 17010004, sum_m_date__year=year, sum_m_date__month=month).aggregate(Sum('sum_m_sale')).values())[0]   #預購正官庄高麗蔘野櫻莓飲
    sum17010002m = list(SumMonthly.objects.filter(prd_code = 17010002, sum_m_date__year=year, sum_m_date__month=month).aggregate(Sum('sum_m_sale')).values())[0]   #預購正官庄高麗蔘精ＥＶＥ / ＲＹＴＩＭＥ１０ｍｌ＊３０入
    
    context.update({'sum11530035m':sum11530035m, 'sum11060162m':sum11060162m, 'sum17010087m':sum17010087m, 'sum17010088m':sum17010088m, 'sum17010004m':sum17010004m, 'sum17010002m':sum17010002m})
    
    # 전년도 전체 판매량 (previous year)
    sum11530035py = list(SumMonthly.objects.filter(prd_code = 11530035, sum_m_date__year=year-1).aggregate(Sum('sum_m_sale')).values())[0]   #正官庄活蔘２８Ｄ高麗蔘活 / 力飲１００ｍｌ＊１０瓶
    sum11060162py = list(SumMonthly.objects.filter(prd_code = 11060162, sum_m_date__year=year-1).aggregate(Sum('sum_m_sale')).values())[0]   #正官庄高麗蔘精ＥＶＥＲＹ / ＴＩＭＥ－秘１０ｍｌ＊２０入
    sum17010087py = list(SumMonthly.objects.filter(prd_code = 17010087, sum_m_date__year=year-1).aggregate(Sum('sum_m_sale')).values())[0]   #預購正官庄活蔘２８Ｄ高麗 / 蔘活力飲禮盒１００ｍｌ＊８入
    sum17010088py = list(SumMonthly.objects.filter(prd_code = 17010088, sum_m_date__year=year-1).aggregate(Sum('sum_m_sale')).values())[0]   #預購正官庄高麗蔘石榴飲 / ５０ｍｌ＊９入
    sum17010004py = list(SumMonthly.objects.filter(prd_code = 17010004, sum_m_date__year=year-1).aggregate(Sum('sum_m_sale')).values())[0]   #預購正官庄高麗蔘野櫻莓飲
    sum17010002py = list(SumMonthly.objects.filter(prd_code = 17010002, sum_m_date__year=year-1).aggregate(Sum('sum_m_sale')).values())[0]   #預購正官庄高麗蔘精ＥＶＥ / ＲＹＴＩＭＥ１０ｍｌ＊３０入
    # **제품이 추가될때마다 코드추가**
    if sum11530035py is None:
        sum11530035py = 1
    if sum11060162py is None:
        sum11060162py = 1
    if sum17010087py is None:
        sum17010087py = 1
    if sum17010088py is None:
        sum17010088py = 1
    if sum17010004py is None:
        sum17010004py = 1
    if sum17010002py is None:
        sum17010002py = 1
    
    # TOP CARD INFO (4)
    # 전상품 연간목표 판매량(또는 금액) = 목표량(target_qauntity) * 12 (또는 월간 목표량 합)
    targetQauntity = list(Dashboard_Table_month_basic.objects.filter(date__year=year).aggregate(Sum('target_qauntity')).values())[0]
    if targetQauntity is None:
        targetQauntity = 1
    ## 전년도    
    targetQauntityPy = list(Dashboard_Table_month_basic.objects.filter(date__year=year-1).aggregate(Sum('target_qauntity')).values())[0]
    if targetQauntityPy is None:
        targetQauntityPy = 1
    
    # 전상품 연간누적 판매량(또는 금액) = Monthly 판매량 합계
    annualSum = list(sum11530035.values())[0] + list(sum11060162.values())[0] + list(sum17010087.values())[0] + list(sum17010088.values())[0] +list(sum17010004.values())[0] + list(sum17010002.values())[0]
    # **제품이 추가될때마다 코드추가**
    if annualSum is None:    
        annualSum = 1
    ## 전년도
    annualSumPy = sum11530035py + sum11060162py + sum17010087py + sum17010088py + sum17010004py + sum17010002py
    # **제품이 추가될때마다 코드추가**
    if annualSumPy is None:
        annualSumPy = 1
    
    
    # 판매진도율 = (누적/목표)*100 (%) : 둘째자리 반올림
    salesRate = round((annualSum/targetQauntity)*100, 2)
    if salesRate is None:
        salesRate = 1
    ## 전년도
    salesRatePy = round((annualSumPy/targetQauntityPy)*100, 2)
    if salesRatePy is None:
        salesRatePy = 1
    
    # 전년비 판매진도율 = ((당해진도율-전년진도율)/전년진도율) * 100 : 둘째자리 반올림
    yoySalesRate = round(((salesRate-salesRatePy)/salesRatePy)*100,2)
    
    context.update({'annualSum':annualSum, 'annualSumPy':annualSumPy, 'targetQauntity':targetQauntity, 'annualSum':annualSum, 'salesRate':salesRate, 'yoySalesRate':yoySalesRate})
    
    
    # 상품별 연간 판매 목표량 대비 실적 (바차트) target_qauntity
    # 당해 목표량
    targetQauntity11530035 = list(Dashboard_Table_month_basic.objects.filter(product_selling_price_id_id__product_id = 11530035, date__year=year).select_related('product_selling_price_id').aggregate(Sum('target_qauntity')).values())[0]
    targetQauntity11060162 = list(Dashboard_Table_month_basic.objects.filter(product_selling_price_id_id__product_id = 11060162, date__year=year).select_related('product_selling_price_id').aggregate(Sum('target_qauntity')).values())[0]
    targetQauntity17010087 = list(Dashboard_Table_month_basic.objects.filter(product_selling_price_id_id__product_id = 17010087, date__year=year).select_related('product_selling_price_id').aggregate(Sum('target_qauntity')).values())[0]
    targetQauntity17010088 = list(Dashboard_Table_month_basic.objects.filter(product_selling_price_id_id__product_id = 17010088, date__year=year).select_related('product_selling_price_id').aggregate(Sum('target_qauntity')).values())[0]
    targetQauntity17010004 = list(Dashboard_Table_month_basic.objects.filter(product_selling_price_id_id__product_id = 17010004, date__year=year).select_related('product_selling_price_id').aggregate(Sum('target_qauntity')).values())[0]
    targetQauntity17010002 = list(Dashboard_Table_month_basic.objects.filter(product_selling_price_id_id__product_id = 17010002, date__year=year).select_related('product_selling_price_id').aggregate(Sum('target_qauntity')).values())[0]
    
    if targetQauntity11530035 is None:
        targetQauntity11530035 = 1
    if targetQauntity11060162 is None:
        targetQauntity11060162 = 1
    if targetQauntity17010087 is None:
        targetQauntity17010087 = 1
    if targetQauntity17010088 is None:
        targetQauntity17010088 = 1
    if targetQauntity17010004 is None:
        targetQauntity17010004 = 1
    if targetQauntity17010002 is None:
        targetQauntity17010002 = 1    
        
    # 당해실적 (monthly 판매량 합)
    sum11530035b = list(sum11530035.values())[0]   #正官庄活蔘２８Ｄ高麗蔘活 / 力飲１００ｍｌ＊１０瓶
    sum11060162b = list(sum11060162.values())[0]   #正官庄高麗蔘精ＥＶＥＲＹ / ＴＩＭＥ－秘１０ｍｌ＊２０入
    sum17010087b = list(sum17010087.values())[0]   #預購正官庄活蔘２８Ｄ高麗 / 蔘活力飲禮盒１００ｍｌ＊８入
    sum17010088b = list(sum17010088.values())[0]   #預購正官庄高麗蔘石榴飲 / ５０ｍｌ＊９入
    sum17010004b = list(sum17010004.values())[0]   #預購正官庄高麗蔘野櫻莓飲
    sum17010002b = list(sum17010002.values())[0]   #預購正官庄高麗蔘精ＥＶＥ / ＲＹＴＩＭＥ１０ｍｌ＊３０入
    
    if sum11530035b is None:
        sum11530035b = 1
    if sum11060162b is None:
        sum11060162b = 1
    if sum17010087b is None:
        sum17010087b = 1
    if sum17010088b is None:
        sum17010088b = 1
    if sum17010004b is None:
        sum17010004b = 1
    if sum17010002b is None:
        sum17010002b = 1
    
    # 진도율 = (누적/목표)*100 (%)
    pct11530035 = round(sum11530035b/targetQauntity11530035,2)*100
    pct11060162 = round(sum11060162b/targetQauntity11060162,2)*100
    pct17010087 = round(sum17010087b/targetQauntity17010087,2)*100
    pct17010088 = round(sum17010088b/targetQauntity17010088,2)*100
    pct17010004 = round(sum17010004b/targetQauntity17010004,2)*100
    pct17010002 = round(sum17010002b/targetQauntity17010002,2)*100
    # **제품이 추가될때마다 코드추가**
    
    # 전년실적
    
    # 전년비 = ((당해판매량-전년판매량)/전년판매량) * 100 (%)
    yoy11530035 = round(((sum11530035b - sum11530035py)/sum11530035py)*100,2)
    yoy11060162 = round(((sum11060162b - sum11060162py)/sum11060162py)*100,2)
    yoy17010087 = round(((sum17010087b - sum17010087py)/sum17010087py)*100,2)
    yoy17010088 = round(((sum17010088b - sum17010088py)/sum17010088py)*100,2)
    yoy17010004 = round(((sum17010004b - sum17010004py)/sum17010004py)*100,2)
    yoy17010002 = round(((sum17010002b - sum17010002py)/sum17010002py)*100,2)
     
    context.update({'targetQauntity11530035':targetQauntity11530035, 'targetQauntity11060162':targetQauntity11060162, 'targetQauntity17010087':targetQauntity17010087,
                    'targetQauntity17010088':targetQauntity17010088, 'targetQauntity17010004':targetQauntity17010004, 'targetQauntity17010002':targetQauntity17010002,
                    'sum11530035b':sum11530035b, 'sum11060162b':sum11060162b, 'sum17010087b':sum17010087b, 'sum17010088b':sum17010088b, 'sum17010004b':sum17010004b, 'sum17010002b':sum17010002b,
                    'pct11530035':pct11530035, 'pct11060162':pct11060162, 'pct17010087':pct17010087, 'pct17010088':pct17010088, 'pct17010004':pct17010004, 'pct17010002':pct17010002,
                    'yoy11530035':yoy11530035, 'yoy11060162':yoy11060162, 'yoy17010087':yoy17010087, 'yoy17010088':yoy17010088, 'yoy17010004':yoy17010004, 'yoy17010002':yoy17010002})
    
    
    # 상품별 연간 목표/전망/실적 요약(표)
    # 제품, 당해목표 (target_qauntity), 당해전망 (expect_qauntity)
    data = list(Dashboard_Table_month_basic.objects.filter(date__year=year).select_related('product_selling_price_id').values('product_selling_price_id__product_id__prd_name').annotate(Sum('target_qauntity'),Sum('expect_qauntity')))
    # 목표비 = (목표/전망) * 100 (%) => 템플릿에서 계산

    context.update({'data':data})
    
    
    # 지역별 전체 판매량 (pie chart)
    sumNor = list(SumMonthly.objects.filter(sum_m_date__year=year,str_code_id__str_loc__contains='北部').select_related('str_code_id').aggregate(Sum('sum_m_sale')).values())[0]
    sumMid = list(SumMonthly.objects.filter(sum_m_date__year=year,str_code_id__str_loc__contains='中部').select_related('str_code_id').aggregate(Sum('sum_m_sale')).values())[0]
    sumSou = list(SumMonthly.objects.filter(sum_m_date__year=year,str_code_id__str_loc__contains='南部').select_related('str_code_id').aggregate(Sum('sum_m_sale')).values())[0]
    sumEas = list(SumMonthly.objects.filter(sum_m_date__year=year,str_code_id__str_loc__contains='東部').select_related('str_code_id').aggregate(Sum('sum_m_sale')).values())[0]
    sumIsl = list(SumMonthly.objects.filter(sum_m_date__year=year,str_code_id__str_loc__contains='外島').select_related('str_code_id').aggregate(Sum('sum_m_sale')).values())[0]
    
    context.update({'sumNor':sumNor, 'sumMid':sumMid, 'sumSou':sumSou, 'sumEas':sumEas, 'sumIsl':sumIsl})
    

    return render(request, 'dashboard/dashboard.html', context)


def create_price(request):
    template = 'dashboard/create_price.html'
    form = Product_selling_priceForm(request.POST or None)

    if form.is_valid():
        form.save()
        messages.success(request, "Registered Succesfully !")
        return HttpResponseRedirect('/dashboard/')

    context = {"form": form}

    return render(request, template, context)


def create_month(request):
    pass

def twmap(request):
    return render(request, 'dashboard/index.html')