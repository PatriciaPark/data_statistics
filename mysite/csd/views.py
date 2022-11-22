from django.shortcuts import render, redirect
from .models import *
from datetime import datetime as dt
from django.core.files.storage import FileSystemStorage
import openpyxl
from pandas import DataFrame
from django.db.models import Sum

# Create your views here.
def index(request):
    # invoiceDaily = InvoiceDaily.objects.all()
    # product = Product.objects.all().prefetch_related('prd_code')
    # store = Store.objects.all().prefetch_related('str_code')
    # total_price = InvoiceDaily.objects.filter(prd_code=11530035).aggregate(Sum('price'))

    invoiceDaily = InvoiceDaily.objects.select_related('prd_code', 'str_code').all()
    context = {"invoiceDaily":invoiceDaily}
    print(context)
    return render(request, 'csd/index.html', context)

def upload(request):
    # try:
    if request.method == 'POST' and request.FILES['fileInput']:
        file = request.FILES['fileInput']
        fs = FileSystemStorage()
        filename = fs.save(file.name.replace(" " , ""), file)
        uploaded_file_url = fs.url(filename)
        excel_file = uploaded_file_url
        print("************************excel_file ", excel_file.encode('utf8').decode('utf8'))
        wb = openpyxl.load_workbook("."+excel_file, data_only=True)
        ws = wb.worksheets[0]
        #시트 이름 가져오기
        sheetname = wb.sheetnames
        grade_dic = {}
        # Converting a worksheet to a Dataframe
        data = ws.values
        
        # print("************************sheetname " +sheetname)

        # 필드명(첫행) 뽑아내어 cols에 넣어주고 뽑아낸 행은 data에서 삭제된다.
        # 여기서 next()는 한행 한행 iter 해주는 역할을 하고
        # [0:]은 필드를 col기준 어디서부터 선택할 것인지이다. 예)[1:]는 두번째 col부터 선택

        cols = next(data)[0:]
        cols = next(data)[0:]
        cols = next(data)[0:]
        cols = next(data)[0:]
        cols = next(data)[0:]
        df = DataFrame(data, columns=cols)
        
        date_month  = str(sheetname[0].split('.')[0])
        print("int(sheetname[0].split('.')[1]): ", date_month)
        date_day    = str(sheetname[0].split('.')[1])
        print("int(sheetname[0].split('.')[0]): ", date_day)
        date_year = str(int(str(ws.cell(row=2,column=1).value).split("：")[1].split("年")[0].strip())+1911)
        print(date_year)

        date_y_m_d = date_year + "-" + date_month + "-" + date_day
        print("date_y_m_d: ", date_y_m_d)    
        fromdate_time_obj = dt.strptime(date_y_m_d, '%Y-%m-%d')
        print("fromdate_time_obj: ",fromdate_time_obj)
        #format_data = "%d/%m/%y %H:%M:%S.%f"

        for dbframe in df.itertuples():

            product = Product.objects.get(prd_code = str(dbframe.貨號))
            
            try:
                store = Store.objects.get(str_code = str(dbframe.門市代號))
            except store.DoesNotExist:
                store = None
      
            obj = InvoiceDaily.objects.create(
                inv_d_date    = fromdate_time_obj,
                inv_d_save    = dbframe.上存量,
                inv_d_buy     = dbframe.進貨量,
                inv_d_return  = dbframe.退貨量,
                inv_d_sale    = dbframe.銷貨量,
                inv_d_stock   = dbframe.庫存量,
                prd_code = product,
                str_code = store
                )
            obj.save()
            
    # except:
    #     message = 'An unknown error occurred.'
    #     return render(request, 'main/error.html',{"message": message})
        
    return redirect('/csd/')