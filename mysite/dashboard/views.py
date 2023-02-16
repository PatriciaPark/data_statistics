from django.shortcuts import render, redirect
from csd.models import *
from django.contrib import messages
from datetime import datetime
from pandas import DataFrame
# from .models import
import pandas as pd
from plotly.offline import plot
import plotly.express as px
from .forms import Product_selling_priceForm, Dashboard_Table_month_basicForm
from django.http import HttpResponseRedirect
from .models import Dashboard_Table_month_basic, Product_selling_price
from django.db.models import Q
from csm.models import SumMonthly
from django.db.models import Sum

# Create your views here.
# index
def index(request):
    # html에서 선택한 연도도 받아오기
    try:
        year = int(request.GET.get('input-year'))
    except TypeError:
        year = int(datetime.today().year)
    
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
    
    context = {'year':year, 'sumSale01':sumSale01, 'sumSale02':sumSale02, 'sumSale03':sumSale03, 'sumSale04':sumSale04, 'sumSale05':sumSale05, 'sumSale06':sumSale06, 
               'sumSale07':sumSale07, 'sumSale08':sumSale08, 'sumSale09':sumSale09, 'sumSale10':sumSale10, 'sumSale11':sumSale11, 'sumSale12':sumSale12}
    
    # 전체 판매량 제품 비율 (파이차트)
    sum11530035 = SumMonthly.objects.filter(prd_code = 11530035, sum_m_date__year=year).aggregate(Sum('sum_m_sale'))   #正官庄活蔘２８Ｄ高麗蔘活 / 力飲１００ｍｌ＊１０瓶
    sum11060162 = SumMonthly.objects.filter(prd_code = 11060162, sum_m_date__year=year).aggregate(Sum('sum_m_sale'))   #正官庄高麗蔘精ＥＶＥＲＹ / ＴＩＭＥ－秘１０ｍｌ＊２０入
    sum17010087 = SumMonthly.objects.filter(prd_code = 17010087, sum_m_date__year=year).aggregate(Sum('sum_m_sale'))   #預購正官庄活蔘２８Ｄ高麗 / 蔘活力飲禮盒１００ｍｌ＊８入
    sum17010088 = SumMonthly.objects.filter(prd_code = 17010088, sum_m_date__year=year).aggregate(Sum('sum_m_sale'))   #預購正官庄高麗蔘石榴飲 / ５０ｍｌ＊９入
    sum17010004 = SumMonthly.objects.filter(prd_code = 17010004, sum_m_date__year=year).aggregate(Sum('sum_m_sale'))   #預購正官庄高麗蔘野櫻莓飲
    sum17010002 = SumMonthly.objects.filter(prd_code = 17010002, sum_m_date__year=year).aggregate(Sum('sum_m_sale'))   #預購正官庄高麗蔘精ＥＶＥ / ＲＹＴＩＭＥ１０ｍｌ＊３０入
    # **제품이 추가될때마다 코드추가**
    
    context.update({'sum11530035':sum11530035, 'sum11060162':sum11060162, 'sum17010087':sum17010087, 'sum17010088':sum17010088, 
                    'sum17010004':sum17010004, 'sum17010002':sum17010002})
    
    
    
    
    
   


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

