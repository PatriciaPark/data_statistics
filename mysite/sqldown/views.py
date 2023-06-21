from django.shortcuts import render
from datetime import datetime

# Create your views here.
def index(request):
    # html에서 선택한 연도도 받아오기
    
    date = request.GET.get('input-date')
    if date is None:
        date = datetime.today().date()

    print(date)
    
    context = {'date':date}
    
    return render(request, 'sqldown/index.html', context)