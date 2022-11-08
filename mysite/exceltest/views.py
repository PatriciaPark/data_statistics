from django.shortcuts import render,redirect
from http.client import HTTPResponse
from .models import SampleModel
import json
import openpyxl

# Create your views here.

# class ExcelUploadView(Views):
def list(request):
    excels = SampleModel.objects.all().order_by('id')
    return render(request, 'index2.html', {'excels':excels})


def post(self, request):
        excelFile = request.FILES['file']

        excel = openpyxl.load_workbook(excelFile, data_only=True)
        work_sheet = excel.worksheets[0]

        all_values = []
        for row in work_sheet.rows:
            row_value = []
            for cell in row:
                row_value.append(cell.value)
            all_values.append(row_value)

        for row in all_values:
            sample_model = SampleModel(Number=row[0], Name=row[1], Item=row[2])
            sample_model.save()

        response = {'status': 1, 'message': '엑셀파일이 정상적으로 업로드 됐습니다.'}
        return HTTPResponse(json.dumps(response), content_type='application/json')