#-*-coding: utf-8
from django.shortcuts import render, redirect
from .models import *
from datetime import datetime as dt
from django.core.files.storage import FileSystemStorage
import openpyxl
from pandas import DataFrame
from django.db.models import Sum
import re


# Create your views here.
def index(request):
    
    sumDaily = SumDaily.objects.select_related('prd_code', 'str_code').all()
    context = {"sumDaily":sumDaily}
    print("**********context ")
    
    return render(request, 'csd/index.html', context)

def upload(request):
    if request.method == 'POST' and request.FILES['fileInput']:
        file = request.FILES['fileInput']
        fs = FileSystemStorage()
        filename = fs.save(file.name.replace(" " , ""), file)
        # uploaded_file_url = fs.url(filename)
        # excel_file = uploaded_file_url
        # 파일명에 한자가 들어가 있으면 위 코드 사용시 인코딩 문제로 에러 발생
        excel_file = '/media/'+ filename
        
        wb = openpyxl.load_workbook("."+excel_file, data_only=True)
        ws = wb.worksheets[1]
        #시트 이름 가져오기
        sheetname = wb.sheetnames
        grade_dic = {}
        # Converting a worksheet to a Dataframe
        data = ws.values
        
        print("************************wb.worksheets[0] ",wb.worksheets[0])
        print("************************wb.worksheets[1] ",wb.worksheets[1])
        print("************************sheetname ", len(sheetname))

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
            print("int(sheetname[i].split('.')[1]): ", date_month)
            date_day    = str(sheetname[i].split('.')[1])
            print("int(sheetname[i].split('.')[0]): ", date_day)
            date_year = str(int(str(ws.cell(row=2,column=1).value).split("：")[1].split("年")[0].strip())+1911)
            print(date_year)

            date_y_m_d = date_year + "-" + date_month + "-" + date_day
            print("date_y_m_d: ", date_y_m_d)    
            fromdate_time_obj = dt.strptime(date_y_m_d, '%Y-%m-%d')
            print("fromdate_time_obj: ",fromdate_time_obj)

            # 데이터 DB 저장
            for dbframe in df.itertuples():
                # 제품/매장 테이블에서 외래키 참조
                product = Product.objects.get(prd_code = str(dbframe.貨號))
                try:
                    store = Store.objects.get(str_code = str(dbframe.門市代號))
                except store.DoesNotExist:
                    store = None
                    
                # 일일 데이터 DB 저장 (tbl_invoice_d)
                obj = InvoiceDaily.objects.create(
                    inv_d_date  = fromdate_time_obj,
                    inv_d_save  = dbframe.上存量,
                    inv_d_buy   = dbframe.進貨量,
                    inv_d_return= dbframe.退貨量,
                    inv_d_sale  = dbframe.銷貨量,
                    inv_d_stock = dbframe.庫存量,
                    prd_code    = product,
                    str_code    = store
                    )
                obj.save()
                
            # 엑셀 합계 데이터 들어있는 셀 읽어오기 (F4~J4)
            d_save  = wb.worksheets[i]["F4"].value
            d_buy   = wb.worksheets[i]["G4"].value
            d_return= wb.worksheets[i]["H4"].value
            d_sale  = wb.worksheets[i]["I4"].value
            d_stock = wb.worksheets[i]["J4"].value
            
            # 합계 데이터 DB 저장 (tbl_sum_d)
            obj_sum = SumDaily.objects.create(
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