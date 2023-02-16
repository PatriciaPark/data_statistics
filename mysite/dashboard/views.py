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
    # html에서 선택한 날짜 받아오기
    try:
        date = request.GET.get('input-month')   #2022-11
        year = request.GET.get('input-year')
        # year = date[:4]     #2022
        month = date[5:]    #11
    except TypeError:
        year = datetime.today().year
        month = '1'

    ####################################################
    
    sumSale01 = SumMonthly.objects.filter(sum_m_date__year=int(2022), sum_m_date__month=1).aggregate(Sum('sum_m_sale'))
    sumSale02 = SumMonthly.objects.filter(sum_m_date__year=int(2022), sum_m_date__month=2).aggregate(Sum('sum_m_sale'))
    sumSale03 = SumMonthly.objects.filter(sum_m_date__year=int(2022), sum_m_date__month=3).aggregate(Sum('sum_m_sale'))
    sumSale04 = SumMonthly.objects.filter(sum_m_date__year=int(2022), sum_m_date__month=4).aggregate(Sum('sum_m_sale'))
    sumSale05 = SumMonthly.objects.filter(sum_m_date__year=int(2022), sum_m_date__month=5).aggregate(Sum('sum_m_sale'))
    sumSale06 = SumMonthly.objects.filter(sum_m_date__year=int(2022), sum_m_date__month=6).aggregate(Sum('sum_m_sale'))
    sumSale07 = SumMonthly.objects.filter(sum_m_date__year=int(2022), sum_m_date__month=7).aggregate(Sum('sum_m_sale'))
    sumSale08 = SumMonthly.objects.filter(sum_m_date__year=int(2022), sum_m_date__month=8).aggregate(Sum('sum_m_sale'))
    sumSale09 = SumMonthly.objects.filter(sum_m_date__year=int(2022), sum_m_date__month=9).aggregate(Sum('sum_m_sale'))
    sumSale10 = SumMonthly.objects.filter(sum_m_date__year=int(2022), sum_m_date__month=10).aggregate(Sum('sum_m_sale'))
    sumSale11 = SumMonthly.objects.filter(sum_m_date__year=int(2022), sum_m_date__month=11).aggregate(Sum('sum_m_sale'))
    sumSale12 = SumMonthly.objects.filter(sum_m_date__year=int(2022), sum_m_date__month=12).aggregate(Sum('sum_m_sale'))
    
    
    
    
    
    
    
    
    
    print('******************',sumSale01)
    
    #################################################### 


    # DB에서 상품별 합계 데이터 받아오기
    prd11530035 = list(SumDaily.objects.filter(prd_code = 11530035, sum_d_date__year=int(year), sum_d_date__month=int(month)).select_related('prd_code').order_by('sum_d_date')) #正官庄活蔘２８Ｄ高麗蔘活 / 力飲１００ｍｌ＊１０瓶
    prd11060162 = list(SumDaily.objects.filter(prd_code = 11060162, sum_d_date__year=int(year), sum_d_date__month=int(month)).select_related('prd_code').order_by('sum_d_date')) #正官庄高麗蔘精ＥＶＥＲＹ / ＴＩＭＥ－秘１０ｍｌ＊２０入
    prd17010087 = list(SumDaily.objects.filter(prd_code = 17010087, sum_d_date__year=int(year), sum_d_date__month=int(month)).select_related('prd_code').order_by('sum_d_date')) #預購正官庄活蔘２８Ｄ高麗 / 蔘活力飲禮盒１００ｍｌ＊８入
    prd17010088 = list(SumDaily.objects.filter(prd_code = 17010088, sum_d_date__year=int(year), sum_d_date__month=int(month)).select_related('prd_code').order_by('sum_d_date')) #預購正官庄高麗蔘石榴飲 / ５０ｍｌ＊９入
    prd17010004 = list(SumDaily.objects.filter(prd_code = 17010004, sum_d_date__year=int(year), sum_d_date__month=int(month)).select_related('prd_code').order_by('sum_d_date')) #預購正官庄高麗蔘野櫻莓飲
    prd17010002 = list(SumDaily.objects.filter(prd_code = 17010002, sum_d_date__year=int(year), sum_d_date__month=int(month)).select_related('prd_code').order_by('sum_d_date')) #預購正官庄高麗蔘精ＥＶＥ / ＲＹＴＩＭＥ１０ｍｌ＊３０入
    prdlist     = list(SumDaily.objects.filter(prd_code = 12345678, sum_d_date__year=int(year), sum_d_date__month=int(month)).select_related('prd_code').order_by('sum_d_date'))

    # product_selling_price_id = models.ForeignKey(Product_selling_price, null=True, on_delete = models.SET_NULL) #제품명과 판매가

    dashboard_data = Dashboard_Table_month_basic.objects.filter(date__year=int(year), date__month=(int(month))).order_by('product_selling_price_id__product_id__prd_code')
    current_year = int(year)
    current_month = int(month)

    # for x in dashboard_data:
    #     print('**************************')
    #     print('dashboard_data:', x.product_selling_price_id.product_id.prd_code)
    #     print('**************************')

    products = [prd11060162, prd11530035, prd17010002, prd17010004, prd17010087, prd17010088,]
    #순서가 중요->오름차순->아래 가져오는 것들도 오름차순으로 정렬

    #당월 누적 판매량(당월실적_양)_[제품별]
    monthly_acc_sum_q = []

    for product in products:
        monthly_product_sum = 0
        for item in product:
            monthly_product_sum += item.sum_d_sale
        monthly_acc_sum_q.append(monthly_product_sum)

    #당월 누적 매출(당월실적_금액)_[제품별]
    monthly_acc_sum_s = []
    this_year_Product_selling_price_list = list(Product_selling_price.objects.filter(year__year = current_year ).order_by('product_id__prd_code',))

    for idx, quantity in enumerate(monthly_acc_sum_q):
        price = this_year_Product_selling_price_list[idx].selling_price
        monthly_total_sum = quantity * price
        monthly_acc_sum_s.append(monthly_total_sum)

    #전년_동월_실제_판매량
    products_code = [11060162, 11530035, 17010002, 17010004, 17010087, 17010088, ]#순서가 중요->오름차순->아래 가져오는 것들도 오름차순으로 정렬
    last_year_month_q =[]

    for product_code in products_code:
        last_year_monthly_sum_by_product = SumMonthly.objects.filter(prd_code = product_code, sum_m_date__year=(int(year)-1), sum_m_date__month=int(month)).select_related('prd_code').order_by('sum_m_date')
        last_year_monthly_sum_by_product_sum = 0
        for item in last_year_monthly_sum_by_product:
            last_year_monthly_sum_by_product_sum += item.sum_m_sale
        last_year_month_q.append(last_year_monthly_sum_by_product_sum)

    #전년_동월_실제_매출
    last_year_month_s =[]

    for idx, quantity in enumerate(last_year_month_q):
        price = this_year_Product_selling_price_list[idx].selling_price
        monthly_total_sum = quantity * price
        last_year_month_s.append(monthly_total_sum)

    # 금월_진도율_판매량
    mothly_ratio_q =[]

    for idx, product in enumerate(dashboard_data):
        ratio = monthly_acc_sum_q[idx] / product.target_qauntity *100
        mothly_ratio_q.append(ratio)

    # 금월_진도율_매출
    mothly_ratio_s =[]
    for idx, product in enumerate(dashboard_data):
        ratio = monthly_acc_sum_s[idx] / product.target_sales *100
        mothly_ratio_s.append(ratio)

    #목표비_판매량_비율
    expect_target_ratio_q = []

    for product in dashboard_data:
        ratio = product.expect_qauntity / product.target_qauntity * 100
        expect_target_ratio_q.append(ratio)

    # 목표비_매출_비율
    expect_target_ratio_s = []

    for product in dashboard_data:
        ratio = product.expect_sales / product.target_sales * 100
        expect_target_ratio_s.append(ratio)

    # #전년비_예상_판매량_비율
    yoy_ratio_q = []

    for idx, product in enumerate(dashboard_data):
        if last_year_month_q[idx]:
            ratio = product.expect_qauntity / last_year_month_q[idx] * 100
            yoy_ratio_q.append(ratio)

    #전년비_예상_매출_비율
    yoy_ratio_s = []

    for idx, product in enumerate(dashboard_data):
        if last_year_month_s[idx]:
            ratio = product.expect_sales / last_year_month_s[idx] * 100
            yoy_ratio_s.append(ratio)

    # print('**************************')
    # print('yoy_ratio_s:', yoy_ratio_s)
    # print('**************************')


    projects_data_1 = [
        {
            'sum_d_code': x.sum_d_code,
            'sum_d_date': x.sum_d_date,
            'sum_d_save': x.sum_d_save,
            'sum_d_buy': x.sum_d_buy,
            'sum_d_return': x.sum_d_return,
            'sum_d_sale': x.sum_d_sale,
            'sum_d_stock': x.sum_d_stock,
            'prd_code': x.prd_code.prd_name,
        } for x in prd11530035
    ]

    # projects_data_1['prd_code'] = json.dumps(projects_data_1['prd_code'])

    projects_data_2 = [
        {
            'sum_d_code': x.sum_d_code,
            'sum_d_date': x.sum_d_date,
            'sum_d_save': x.sum_d_save,
            'sum_d_buy': x.sum_d_buy,
            'sum_d_return': x.sum_d_return,
            'sum_d_sale': x.sum_d_sale,
            'sum_d_stock': x.sum_d_stock,
            'prd_code': x.prd_code.prd_name,
        } for x in prd11060162
    ]

    # projects_data_2['prd_code'] = json.dumps(projects_data_2['prd_code'])

    projects_data_3 = [
        {
            'sum_d_code': x.sum_d_code,
            'sum_d_date': x.sum_d_date,
            'sum_d_save': x.sum_d_save,
            'sum_d_buy': x.sum_d_buy,
            'sum_d_return': x.sum_d_return,
            'sum_d_sale': x.sum_d_sale,
            'sum_d_stock': x.sum_d_stock,
            'prd_code': x.prd_code.prd_name,
        } for x in prd17010087
    ]
    # projects_data_3['prd_code'] = json.dumps(projects_data_3['prd_code'])

    projects_data_4 = [
        {
            'sum_d_code': x.sum_d_code,
            'sum_d_date': x.sum_d_date,
            'sum_d_save': x.sum_d_save,
            'sum_d_buy': x.sum_d_buy,
            'sum_d_return': x.sum_d_return,
            'sum_d_sale': x.sum_d_sale,
            'sum_d_stock': x.sum_d_stock,
            'prd_code': x.prd_code.prd_name,
        } for x in prd17010088
    ]
    # projects_data_4['prd_code'] = json.dumps(projects_data_4['prd_code'])

    projects_data_5 = [
        {
            'sum_d_code': x.sum_d_code,
            'sum_d_date': x.sum_d_date,
            'sum_d_save': x.sum_d_save,
            'sum_d_buy': x.sum_d_buy,
            'sum_d_return': x.sum_d_return,
            'sum_d_sale': x.sum_d_sale,
            'sum_d_stock': x.sum_d_stock,
            'prd_code': x.prd_code.prd_name,
        } for x in prd17010004
    ]
    # projects_data_5['prd_code'] = json.dumps(projects_data_5['prd_code'])

    projects_data_6 = [
        {
            'sum_d_code': x.sum_d_code,
            'sum_d_date': x.sum_d_date,
            'sum_d_save': x.sum_d_save,
            'sum_d_buy': x.sum_d_buy,
            'sum_d_return': x.sum_d_return,
            'sum_d_sale': x.sum_d_sale,
            'sum_d_stock': x.sum_d_stock,
            'prd_code': x.prd_code.prd_name,
        } for x in prd17010002
    ]
    # projects_data_6['prd_code'] = json.dumps(projects_data_6['prd_code'])

    projects_data_7 = [
        {
            'sum_d_code': x.sum_d_code,
            'sum_d_date': x.sum_d_date,
            'sum_d_save': x.sum_d_save,
            'sum_d_buy': x.sum_d_buy,
            'sum_d_return': x.sum_d_return,
            'sum_d_sale': x.sum_d_sale,
            'sum_d_stock': x.sum_d_stock,
            'prd_code': x.prd_code.prd_name,
        } for x in prdlist
    ]
    # projects_data_7['prd_code'] = json.dumps(projects_data_7['prd_code'])

    projects_data_1.extend(projects_data_2)
    projects_data_1.extend(projects_data_3)
    projects_data_1.extend(projects_data_4)
    projects_data_1.extend(projects_data_5)
    projects_data_1.extend(projects_data_6)
    # projects_date = projects_date.extend(projects_data_7)

    # df = pd.DataFrame(projects_date)
    df = pd.DataFrame(projects_data_1)
    # print(df)
    # fig = px.(
    #     df, x_start="sum_d_datev", x_end="Finish", y="prd_code", color="Responsible",
    # )

    # fig.update_yaxes(autorange="reversed")
    # gantt_plot = plot(fig, output_type="div")
    # context={'plot+div': gantt_plot}

    if len(df) != 0 :

        fig1 = px.box(df, x="prd_code", y="sum_d_buy", color="prd_code", title=f"{request.GET.get('input-month')}. product-buy analysis")
        fig2 = px.bar(df, x="sum_d_date", y="sum_d_stock", title=f"{request.GET.get('input-month')}. date-stock analysis")
        fig3 = px.scatter(df, x="sum_d_date", y="sum_d_sale",color="prd_code", title=f"{request.GET.get('input-month')}. date-sale analysis")
        fig4 = px.line(df, x="sum_d_date", y="sum_d_buy", line_group="prd_code",color="prd_code", title=f"{request.GET.get('input-month')}. date-buy analysis")
        fig5 = px.area(df, x="prd_code", y="sum_d_stock", line_group="sum_d_date", color="prd_code", title=f"{request.GET.get('input-month')}. product-stock analysis")#good
        fig6 = px.pie(df, names="prd_code", values="sum_d_return",color="prd_code", title=f"{request.GET.get('input-month')}. product-return analysis") #good
        plot_div1 = plot(fig1, output_type="div")
        plot_div2 = plot(fig2, output_type="div")
        plot_div3 = plot(fig3, output_type="div")
        plot_div4 = plot(fig4, output_type="div")
        plot_div5 = plot(fig5, output_type="div")
        plot_div6 = plot(fig6, output_type="div")

        product_name = []
        target_qauntity = []
        expect_qauntity = []
        for data in dashboard_data:
            product_name.append(data.product_selling_price_id.product_id.prd_name)
            target_qauntity.append(data.target_qauntity)
            expect_qauntity.append(data.expect_qauntity)

        dash_data_list = []

        for data in dashboard_data:

            dash_data_dic ={
                'dashboard_data': data,
                'product_name': product_name[idx],
                'target_qauntity': target_qauntity[idx],
                'expect_qauntity': expect_qauntity[idx],
                'monthly_acc_sum_q': monthly_acc_sum_q[idx],
                'monthly_acc_sum_s': monthly_acc_sum_s[idx],
                'last_year_month_q': last_year_month_q[idx],
                'last_year_month_s': last_year_month_s[idx],
                'mothly_ratio_q': round(mothly_ratio_q[idx],1),
                'mothly_ratio_s':round( mothly_ratio_s[idx],1),
                'expect_target_ratio_q': round(expect_target_ratio_q[idx],1),
                'expect_target_ratio_s': round(expect_target_ratio_s[idx],1),
                'yoy_ratio_q': round(yoy_ratio_q[idx],1),
                'yoy_ratio_s': round(yoy_ratio_s[idx],1),
            }
            dash_data_list.append(dash_data_dic)
            print(dash_data_list)

    # for idx, data in enumerate(dashboard_data):
    #         if idx is not None:
    #             print('**************************')
    #             # print('dashboard_data55:', dashboard_data)
    #             print('idx', idx)
    #             print('**************************')
    #             dash_data_dic ={}
    #             dash_data_dic['dashboard_data']= data,
    #             dash_data_dic['product_name']= product_name[idx],
    #             dash_data_dic['target_qauntity']= target_qauntity[idx],
    #             print('**************************')
    #             # print('dashboard_data55:', dashboard_data)
    #             print('target_qauntity:', target_qauntity[idx])
    #             print('**************************')
    #             print('**************************')
    #             # print('dashboard_data55:', dashboard_data)
    #             print('target_qauntity2:', dash_data_dic['target_qauntity'])
    #             print('**************************')
    #             dash_data_dic['expect_qauntity']= expect_qauntity[idx],
    #             dash_data_dic['monthly_acc_sum_q']= monthly_acc_sum_q[idx],
    #             dash_data_dic['monthly_acc_sum_s']= monthly_acc_sum_s[idx],
    #             dash_data_dic['last_year_month_q']= last_year_month_q[idx],
    #             dash_data_dic['last_year_month_s']= last_year_month_s[idx],
    #             dash_data_dic['mothly_ratio_q']= mothly_ratio_q[idx],
    #             dash_data_dic['mothly_ratio_s']= mothly_ratio_s[idx],
    #             dash_data_dic['expect_target_ratio_q']= expect_target_ratio_q[idx],
    #             dash_data_dic['expect_target_ratio_s']= expect_target_ratio_s[idx],
    #             dash_data_dic['yoy_ratio_q']= yoy_ratio_q[idx],
    #             dash_data_dic['yoy_ratio_s']= yoy_ratio_s[idx],
    #             dash_data_list.append(dash_data_dic)
    #             print(dash_data_list)


        # html 화면에 출력할 데이터 담을 리스트
        context = {
            'plot1': plot_div1,
            'plot2': plot_div2,
            'plot3': plot_div3,
            'plot4': plot_div4,
            'plot5': plot_div5,
            'plot6': plot_div6,

            'current_month': current_month,
            'current_year' : current_year,

            'dash_data_list': dash_data_list,
            # 'month':month, 'prdlist':prdlist, 'prd11530035':prd11530035, 'prd11060162':prd11060162, 'prd17010087':prd17010087, 'prd17010088':prd17010088, 'prd17010004':prd17010004, 'prd17010002':prd17010002

            # 'this_month': dashboard_data.date,
            # 'monthly_target_q': dashboard_data.target_qauntity,
            # 'monthly_target_s': dashboard_data.target_sales,
            # 'monthly_expect_s': dashboard_data.expect_qauntity,
            # 'monthly_expect_s': dashboard_data.expect_sales,

            # 'dashboard_data': dashboard_data,
            # 'product_name': product_name,
            # 'target_qauntity': target_qauntity,
            # 'expect_qauntity': expect_qauntity,
            # 'monthly_acc_sum_q': monthly_acc_sum_q,
            # 'monthly_acc_sum_s': monthly_acc_sum_s,
            # 'last_year_month_q': last_year_month_q ,
            # 'last_year_month_s': last_year_month_s,
            # 'mothly_ratio_q': mothly_ratio_q,
            # 'mothly_ratio_s': mothly_ratio_s,
            # 'expect_target_ratio_q': expect_target_ratio_q,
            # 'expect_target_ratio_s': expect_target_ratio_s,
            # 'yoy_ratio_q': yoy_ratio_q,
            # 'yoy_ratio_s': yoy_ratio_s,
            }
    else:
        context = {
            'current_month': current_month,
            'current_year' : current_year,
            'dash_data_list': dash_data_list,
            # 'dashboard_data': dashboard_data,
            # 'product_name': product_name,
            # 'target_qauntity': target_qauntity,
            # 'expect_qauntity': expect_qauntity,
            # 'current_month': current_month,
            # 'current_year' : current_year,
            # 'monthly_acc_sum_q': monthly_acc_sum_q,
            # 'monthly_acc_sum_s': monthly_acc_sum_s,
            # 'last_year_month_q': last_year_month_q ,
            # 'last_year_month_s': last_year_month_s,
            # 'mothly_ratio_q': mothly_ratio_q,
            # 'mothly_ratio_s': mothly_ratio_s,
            # 'expect_target_ratio_q': expect_target_ratio_q,
            # 'expect_target_ratio_s': expect_target_ratio_s,
            # 'yoy_ratio_q': yoy_ratio_q,
            # 'yoy_ratio_s': yoy_ratio_s,
            # 'month':month, 'prdlist':prdlist, 'prd11530035':prd11530035, 'prd11060162':prd11060162, 'prd17010087':prd17010087, 'prd17010088':prd17010088, 'prd17010004':prd17010004, 'prd17010002':prd17010002
            }

    context.update({'sumSale01':sumSale01, 'sumSale02':sumSale02, 'sumSale03':sumSale03, 'sumSale04':sumSale04, 'sumSale05':sumSale05, 'sumSale06':sumSale06, 
                'sumSale07':sumSale07, 'sumSale08':sumSale08, 'sumSale09':sumSale09, 'sumSale10':sumSale10, 'sumSale11':sumSale11, 'sumSale12':sumSale12})

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

