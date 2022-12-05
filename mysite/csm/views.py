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

    monthData = SumMonthly.objects.filter(sum_d_date__year=int(year), sum_d_date__month=int(month)).select_related('prd_code','str_code')


    # html 화면에 출력할 데이터 담을 리스트                    
    context = {'month':month, 'monthData':monthData}
    
    return render(request, 'csm/index.html', context)

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
      # Converting a worksheet to a Dataframe
      data = ws.values

      # 필드명(첫행) 뽑아내어 cols에 넣어주고 뽑아낸 행은 data에서 삭제된다.
      # 여기서 next()는 한행 한행 iter 해주는 역할을 하고
      # [0:]은 필드를 col기준 어디서부터 선택할 것인지이다. 예)[1:]는 두번째 col부터 선택

      cols = next(data)[0:]
      cols = next(data)[0:]
      cols = next(data)[0:]
      cols = next(data)[0:]
      cols = next(data)[0:]
      df = DataFrame(data, columns=cols)
      
      # date_day    = str(filename[3:5].strip())
      print("filename", filename.split(".")[0].split('_')[0][-2:].strip())
      date_month  = str(filename.split(".")[0].split('_')[0][-2:].strip())
      print('int(filename[-2:]): ', date_month)
      date_year = str(int(str(ws.cell(row=2,column=1).value).split("：")[1].split("年")[0].strip())+1911)
      print('date_year ',date_year)

      date_y_m_d = date_year + "-" + date_month
      print("date_y_m_d: ", date_y_m_d)    
      fromdate_time_obj = datetime.strptime(date_y_m_d, '%Y-%m')
      print("fromdate_time_obj: ",fromdate_time_obj)
              
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
              
          # Save sum data to DB (tbl_sum_m)
          obj_sum, created = SumMonthly.objects.update_or_create(
              sum_m_date  = fromdate_time_obj,
              sum_m_save  = dbframe.上存量,
              sum_m_buy   = dbframe.進貨量,
              sum_m_return= dbframe.退貨量,
              sum_m_sale  = dbframe.銷貨量,
              sum_m_stock = dbframe.庫存量,
              prd_code    = product,
              str_code    = store
              )
          obj_sum.save()
               
    return redirect('/csm/?input-month='+date_year+'-'+date_month)