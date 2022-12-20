from django.shortcuts import render
from datetime import datetime
from .models import SumMonthly

# Create your views here.
def index(request):
  # html에서 선택한 날짜 받아오기
  try:
      year = request.GET.get('input-year')   #2022
  except TypeError:
      year = datetime.today().year
  
  # html에서 선택한 select box value 받아오기 및 정렬
  prdcode = request.GET.get('input-prd')  #상품코드
  
  if prdcode:
    data = SumMonthly.objects.filter(prd_code = prdcode, sum_m_date__year=year).select_related('prd_code','str_code').order_by('sum_m_code','prd_code')
  else:
    data = SumMonthly.objects.filter(sum_m_date__year=year).select_related('prd_code','str_code').order_by('sum_m_code','prd_code')
    
  context = {'yearDate':year, 'data':data}
  
  return render(request, 'csy/index.html', context)