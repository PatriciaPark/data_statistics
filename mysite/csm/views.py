#-*-coding: utf-8
from django.shortcuts import render, redirect
from .models import *
from django.core.files.storage import FileSystemStorage
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from datetime import datetime
from pandas import DataFrame
import openpyxl, calendar


# index
def index(request):
  # html에서 선택한 날짜 받아오기
    try:
        date = request.GET.get('input-month')   #2022-11
        year = date[:4]     #2022
        month = date[5:]    #11
    except TypeError:
        year = datetime.today().year
        month = datetime.today().month

    monthData = SumMonthly.objects.filter(sum_m_date__year=int(year), sum_m_date__month=int(month)).select_related('prd_code','str_code')
        
    # html 화면에 출력할 데이터 담을 리스트                    
    context = {'month':month, 'monthData':monthData}

    return render(request, 'csm/index.html', context)

# excel file upload
def upload(request):
    if request.method == 'POST' and request.FILES['fileInput']:
        # file directory
        file = request.FILES['fileInput']
        fs = FileSystemStorage()
        filename = fs.save(file.name.replace(' ' , ''), file)
        excel_file = '/media/'+ filename
        
        # get sheet name
        wb = openpyxl.load_workbook('.'+excel_file, data_only=True)
        ws = wb.worksheets[0]
        sheetname = wb.sheetnames
        
        try:
            for i in range(0, len(sheetname)):
                ws = wb.worksheets[i]
                sheetname = wb.sheetnames
                
                # Converting a worksheet to a Dataframe
                data = ws.values
                cols = next(data)[0:]
                cols = next(data)[0:]
                cols = next(data)[0:]
                cols = next(data)[0:]
                cols = next(data)[0:]
                df = DataFrame(data, columns=cols)
                
                # 날짜 추출      
                date_month  = str(filename.split(".")[0].split('_')[0][-2:].strip())
                date_year = str(int(str(ws.cell(row=2,column=1).value).split("：")[1].split("年")[0].strip())+1911)
                date_y_m = date_year + "-" + date_month
                fromdate_time_obj = datetime.strptime(date_y_m, '%Y-%m')
                
                # 불러온 달의 마지막일 (eg. 28일/30일/31일)
                last_date = calendar.monthrange(int(date_year), int(date_month))[1]
                
                # 데이터 DB 저장
                for dbframe in df.itertuples():
                    # 제품/매장 테이블에서 외래키 참조
                    product, store = 0,0
                    
                    try:
                        product = Product.objects.get(prd_code = str(dbframe.貨號))
                    except ObjectDoesNotExist:
                        product = None
                        
                    try:
                        store = Store.objects.get(str_code = str(dbframe.門市代號))
                    except ObjectDoesNotExist:
                        store = None
                    
                    # 일일 판매량 및 오차율    
                    m_sale  = wb.worksheets[i]['K4'].value # 판매총합 셀
                    dailySale, errorRate = 0, 0
                    dailySale = float(format(m_sale/last_date,".2f"))
                    try : 
                        errorRate = format(dbframe.銷貨量/dailySale,".2f")
                    except ZeroDivisionError:
                        errorRate = None
                    
                    # Save sum data to DB (tbl_sum_m)
                    obj, created = SumMonthly.objects.update_or_create(
                        sum_m_date  = fromdate_time_obj,
                        sum_m_save  = dbframe.上存量,
                        sum_m_buy   = dbframe.進貨量,
                        sum_m_return= dbframe.退貨量,
                        sum_m_sale  = dbframe.銷貨量,
                        sum_m_stock = dbframe.庫存量,
                        sum_m_sale_ttl = dailySale,
                        sum_m_sale_err = errorRate,
                        prd_code    = product,
                        str_code    = store
                        )
                    obj.save()
        except:
            messages.warning(request, 'Invalid file')
            return redirect('/csm/')
    
    return redirect('/csm/?input-month='+date_year+'-'+date_month)