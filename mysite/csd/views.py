from django.shortcuts import render, redirect
from .models import *
from datetime import datetime as dt
from django.core.files.storage import FileSystemStorage
import openpyxl
from pandas import DataFrame

# Create your views here.
def index(request):
  return render(request, 'csd/index.html')

def upload(request):
    # try:
    if request.method == 'POST' and request.FILES['fileInput']:
        file = request.FILES['fileInput']
        fs = FileSystemStorage()
        filename = fs.save(file.name, file)
        uploaded_file_url = fs.url(filename)
        excel_file = uploaded_file_url
        wb = openpyxl.load_workbook("."+excel_file, data_only=True)
        ws = wb.worksheets[1]
        grade_dic = {}
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
        
        date_day    = str(filename[3:5].strip())
        print("int(filename[3:5]): ", date_day)
        date_month  = str(filename[:2].strip())
        print("int(filename[0:2]): ", date_month)
        date_year = str(int(str(ws.cell(row=2,column=1).value).split("：")[1].split("年")[0].strip())+1911)
        print(date_year)

        date_y_m_d = date_year + "-" + date_month + "-" + date_day
        print("date_y_m_d: ", date_y_m_d)    
        fromdate_time_obj = dt.strptime(date_y_m_d, '%Y-%m-%d')
        print("fromdate_time_obj: ",fromdate_time_obj)
        #format_data = "%d/%m/%y %H:%M:%S.%f"

        for dbframe in df.itertuples():

            product = tbl_product.objects.get(product_code_bystore = str(dbframe.貨號))
            store = tbl_store.objects.get(store_code = str(dbframe.門市代號))
      
            obj = tbl_invoice_daily.objects.create(
                invoice_day_date    = fromdate_time_obj,
                invoice_day_save    = dbframe.上存量,
                invoice_day_buy     = dbframe.進貨量,
                invoice_day_return  = dbframe.退貨量,
                invoice_day_sale    = dbframe.銷貨量,
                invoice_day_stock   = dbframe.庫存量,
                invoice_day_product = product,
                invoice_day_store = store
                )
            obj.save()

    # except:
    #     message = 'An unknown error occurred.'
    #     return render(request, 'main/error.html',{"message": message})
        
    return redirect('/index/')