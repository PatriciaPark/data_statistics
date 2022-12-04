#-*-coding: utf-8
from django.shortcuts import render, redirect
from .models import *
import calendar
from datetime import datetime, timedelta
from django.core.files.storage import FileSystemStorage
from django.core.exceptions import ObjectDoesNotExist
import openpyxl
from pandas import DataFrame
import pandas as pd


# Create your views here.
def index(request):
    # html에서 선택한 날짜 받아오기
    try:
        date = request.GET.get('input-month')   #2022-11
        year = date[:4]     #2022
        month = date[5:]    #11
    except TypeError:
        year = datetime.today().year
        month = datetime.today().month
    
    # 불러온 달의 첫째일과 마지막일
    last_date = calendar.monthrange(int(year), int(month))[1]
    first_day = year + '-' + month + '-01'
    last_day = year+'-'+month+'-'+ str(last_date)
    print(first_day, last_day)
    
    # testInx = DataFrame.reindex(dates, fill_value=0)

    # 빈 날짜 찾아서 list 넣기
    nullDate = []
    result = []
    
    def date_range(start, end):
        start = datetime.strptime(start, '%Y-%m-%d')
        end = datetime.strptime(end, '%Y-%m-%d')
        dates = [(start + timedelta(days=i+1)).strftime('%Y-%m-%d') for i in range((end-start).days-1)]
        return dates
    
    
    test = SumDaily.objects.filter(prd_code = 11530035, sum_d_date__year=int(year), sum_d_date__month=int(month)).select_related('prd_code')
    testValues = test.values_list('sum_d_date')
    print('***testValues: ',test)
    df = DataFrame(test)
    # idx = pd.period_range(first_day, last_day)
    print('***dfdfdf: ',df[0][0])
    # df.reindex(idx, fill_value=0)
    df['sum_d_date'] = pd.to_datetime(df['sum_d_date'])
    df = (df.set_index('sum_d_date')
        .reindex(pd.date_range(first_day, last_day, freq='D'))
        .rename_axis(['sum_d_date'])
        .fillna(0)
        .reset_index())
    
    print('***df: ',df)
    
    for i in range(1,len(testValues)):
        dates = date_range(str(testValues.get(pk=i))[15:27].replace(', ', '-').replace(')', ''), str(testValues.get(pk=i+1))[15:27].replace(', ', '-').replace(')', ''))
        #print(dates)
        if dates:
            for j in range(0,len(dates)):
                #print(dates[j])
                nullDate.append(dates[j])
                # result.append(df.reindex(nullDate))
    
        
    #print(str(test.get(pk=1))[15:27].replace(', ', '-').replace(')', ''))
    # sumDaily = SumDaily.objects.select_related('prd_code', 'str_code').all()
    # sumDaily = SumDaily.objects.filter(sum_d_date__year=int(year), sum_d_date__month=int(month)).select_related('prd_code')
    # DB에서 상품별 합계 데이터 받아오기
    prd11530035 = SumDaily.objects.filter(prd_code = 11530035, sum_d_date__year=int(year), sum_d_date__month=int(month)).select_related('prd_code') #正官庄活蔘２８Ｄ高麗蔘活 / 力飲１００ｍｌ＊１０瓶
    prd11060162 = SumDaily.objects.filter(prd_code = 11060162, sum_d_date__year=int(year), sum_d_date__month=int(month)).select_related('prd_code') #正官庄高麗蔘精ＥＶＥＲＹ / ＴＩＭＥ－秘１０ｍｌ＊２０入
    prd17010087 = SumDaily.objects.filter(prd_code = 17010087, sum_d_date__year=int(year), sum_d_date__month=int(month)).select_related('prd_code') #預購正官庄活蔘２８Ｄ高麗 / 蔘活力飲禮盒１００ｍｌ＊８入
    prd17010088 = SumDaily.objects.filter(prd_code = 17010088, sum_d_date__year=int(year), sum_d_date__month=int(month)).select_related('prd_code') #預購正官庄高麗蔘石榴飲 / ５０ｍｌ＊９入
    prd17010004 = SumDaily.objects.filter(prd_code = 17010004, sum_d_date__year=int(year), sum_d_date__month=int(month)).select_related('prd_code') #預購正官庄高麗蔘野櫻莓飲
    prd17010002 = SumDaily.objects.filter(prd_code = 17010002, sum_d_date__year=int(year), sum_d_date__month=int(month)).select_related('prd_code') #預購正官庄高麗蔘精ＥＶＥ / ＲＹＴＩＭＥ１０ｍｌ＊３０入
    
    #results = str(nullDate).replace('[', '').replace(']', '')
    
    print('prd11530035 ',prd11530035)
    # print('result ',result)
    # html 화면에 출력할 데이터 담을 리스트                    
    context = {'month':month,'nullDate':nullDate,'prd11530035':prd11530035, 'prd11060162':prd11060162, 'prd17010087':prd17010087, 'prd17010088':prd17010088, 'prd17010004':prd17010004, 'prd17010002':prd17010002}
    
    return render(request, 'csd/index.html', context)

def upload(request):
    if request.method == 'POST' and request.FILES['fileInput']:
        file = request.FILES['fileInput']
        fs = FileSystemStorage()
        filename = fs.save(file.name.replace(' ' , ''), file)
        # uploaded_file_url = fs.url(filename)
        # excel_file = uploaded_file_url
        # 파일명에 한자가 들어가 있으면 위 코드 사용시 인코딩 문제로 에러 발생
        excel_file = '/media/'+ filename
        
        wb = openpyxl.load_workbook('.'+excel_file, data_only=True)
        ws = wb.worksheets[1]
        #시트 이름 가져오기
        sheetname = wb.sheetnames
        grade_dic = {}
        # Converting a worksheet to a Dataframe
        data = ws.values
        
        #print('************************wb.worksheets[0] ',wb.worksheets[0])
        #print('************************wb.worksheets[1] ',wb.worksheets[1])
        #print('************************sheetname ', len(sheetname))

        # 필드명(첫행) 뽑아내어 cols에 넣어주고 뽑아낸 행은 data에서 삭제된다.
        # 여기서 next()는 한행 한행 iter 해주는 역할을 하고
        # [0:]은 필드를 col기준 어디서부터 선택할 것인지이다. 예)[1:]는 두번째 col부터 선택

        cols = next(data)[0:]
        cols = next(data)[0:]
        cols = next(data)[0:]
        cols = next(data)[0:]
        cols = next(data)[0:]
        df = DataFrame(data, columns=cols)
        
        for i in range(0, len(sheetname)):
            # 엑셀 시트 이름에서 날짜 추출 
            date_month  = str(sheetname[i].split('.')[0])
            date_day    = str(sheetname[i].split('.')[1])
            # 추출한 날짜 형변환
            date_year = str(int(str(ws.cell(row=2,column=1).value).split('：')[1].split('年')[0].strip())+1911)
            date_y_m_d = date_year + '-' + date_month + '-' + date_day
            fromdate_time_obj = datetime.strptime(date_y_m_d, '%Y-%m-%d')
            
            last_date = calendar.monthrange(int(date_year), int(date_month))[1]
            print("******************",last_date)
            
            # date_null = int(date_day)
            # print("iiiiiiiiiiiii ", (i+1), date_null)
            # if i+1 != date_null:
            #     NullDate = i+1
            #     overDate = date_null
            #     print("************NullDate: ", str(NullDate))
            #     date_y_m_d_null = date_year + '-' + date_month + '-' + str(NullDate)
            #     fromdate_time_obj_null = datetime.strptime(date_y_m_d_null, '%Y-%m-%d')
            #     print("fromdate_time_obj_null", fromdate_time_obj_null)
            #     date_null = overDate-1
            #     continue

            
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
                    
                # 일일 데이터 DB 저장 (tbl_invoice_d)
                # obj, created = InvoiceDaily.objects.update_or_create(
                #     inv_d_date  = fromdate_time_obj,
                #     inv_d_save  = dbframe.上存量,
                #     inv_d_buy   = dbframe.進貨量,
                #     inv_d_return= dbframe.退貨量,
                #     inv_d_sale  = dbframe.銷貨量,
                #     inv_d_stock = dbframe.庫存量,
                #     prd_code    = product,
                #     str_code    = store
                #     )
                # obj.save()
                
                # 엑셀 합계 데이터 들어있는 셀 읽어오기 (F4~J4)
                d_save  = wb.worksheets[i]['F4'].value
                d_buy   = wb.worksheets[i]['G4'].value
                d_return= wb.worksheets[i]['H4'].value
                d_sale  = wb.worksheets[i]['I4'].value
                d_stock = wb.worksheets[i]['J4'].value
                
                # Add missing dates to pandas dataframe
                first_day = date_year+'-'+date_month+'-01'
                last_day = date_year+'-'+date_month+'-'+ str(last_date)
                idx = pd.date_range(first_day, last_day, freq='D')
                df.reindex(idx, fill_value=0)
                dfNull = df.reindex(index=idx, columns=['sum_d_save', 'sum_d_buy', 'sum_d_return', 'sum_d_sale', 'sum_d_stock'], fill_value=0)
                
                # Save sum data to DB (tbl_sum_d)
                obj_sum, created = SumDaily.objects.update_or_create(
                    sum_d_date  = fromdate_time_obj,
                    sum_d_save  = d_save,
                    sum_d_buy   = d_buy,
                    sum_d_return= d_return,
                    sum_d_sale  = d_sale,
                    sum_d_stock = d_stock,
                    prd_code    = product,
                    str_code    = store
                    )
                obj_sum.save()
                
            
                # 엑셀 시트에 없는 날짜 추출 및 형변환
                # print("iiiiiiiiiiiii ", (i+1), int(date_day))
                # if i+1 != int(date_day):
                #     NullDate = int(date_day)
                #     print("************NullDate: ", str(NullDate))
                #     date_y_m_d_null = date_year + '-' + date_month + '-' + str(NullDate)
                #     fromdate_time_obj_null = datetime.strptime(date_y_m_d_null, '%Y-%m-%d')
                #     print("fromdate_time_obj_null", fromdate_time_obj_null)
                    
                    # 없는 날짜 데이터 넣기
                    # obj_sum, created = SumDaily.objects.update_or_create(
                    #     sum_d_date  = fromdate_time_obj_null,
                    #     sum_d_save  = 0,
                    #     sum_d_buy   = 0,
                    #     sum_d_return= 0,
                    #     sum_d_sale  = 0,
                    #     sum_d_stock = 0,
                    #     prd_code    = product,
                    #     str_code    = store
                    #     )
                    # obj_sum.save()
                    
                
            
                
            # 직접 합계 계산하는 로직 => 오래걸림
            # sum_save = InvoiceDaily.objects.filter(inv_d_date=date_y_m_d).aggregate(Sum('inv_d_save'))
            # sum_buy = InvoiceDaily.objects.filter(inv_d_date=date_y_m_d).aggregate(Sum('inv_d_buy'))
            # sum_return = InvoiceDaily.objects.filter(inv_d_date=date_y_m_d).aggregate(Sum('inv_d_return'))
            # sum_sale = InvoiceDaily.objects.filter(inv_d_date=date_y_m_d).aggregate(Sum('inv_d_sale'))
            # sum_stock = InvoiceDaily.objects.filter(inv_d_date=date_y_m_d).aggregate(Sum('inv_d_stock'))
            
            # obj2 = SumDaily.objects.create(
            #     sum_d_date  = fromdate_time_obj,
            #     sum_d_save  = sum_save['inv_d_save__sum'],
            #     sum_d_buy   = sum_buy['inv_d_buy__sum'],
            #     sum_d_return= sum_return['inv_d_return__sum'],
            #     sum_d_sale  = sum_sale['inv_d_sale__sum'],
            #     sum_d_stock = sum_stock['inv_d_stock__sum'],
            #     prd_code    = product,
            #     str_code    = store
            # )
            # obj2.save()
        
    return redirect('/csd/')