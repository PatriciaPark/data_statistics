from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from .models import *
from csd.models import Store

# Create your views here.
def index(request):
    
    # get select box value
    getloc = request.GET.get('input-loc')
    getCity = request.GET.get('input-city')
    getStore = request.GET.get('input-str')
    
    # set select box value
    loc = Store.objects.values('str_loc').distinct()
    city = Store.objects.filter(str_loc=getloc).values('str_city').distinct()
    str = Store.objects.filter(str_loc=getloc, str_city=getCity).values('str_name')
    
    # read data
    if getloc is not None and (getCity is None or getCity == 'all') and (getStore is None or getStore == 'all'):
        data = StoreReview.objects.filter(str_code__str_loc=getloc).select_related('str_code').all().order_by('str_code__str_city')
    elif getloc is not None and getCity is not None and (getStore is None or getStore == 'all'):
        data = StoreReview.objects.filter(str_code__str_loc=getloc, str_code__str_city=getCity).select_related('str_code').all().order_by('str_code__str_city')
    else:
        data = StoreReview.objects.select_related('str_code').all().order_by('str_code__str_city')
    
    context = {'loc':loc, 'city':city, 'str':str, 'data':data}
    
    return render(request, 'csr/index.html', context)

# Create store review
def create(request):
    
    # get select box value
    getloc = request.POST.get('info-loc')
    getCity = request.POST.get('info-city')
    getCode = request.POST.get('info-code')
    
    print('Location:', getloc, ', City:', getCity, ', Code:', getCode)
    # 매장 데이터 DB update
    obj = Store.objects.filter(str_code=getCode).update(str_loc=getloc, str_city=getCity)
    
    print('**Updated**', obj)
    
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

# Add Field Select Box
def select(request):
    
    # get select box value
    getloc = request.GET.get('location')
    
    # set select box value
    city = Store.objects.filter(str_loc=getloc).values('str_city').distinct().order_by('str_city')
    
    return JsonResponse({'data': list(city)})

def select2(request):
    
    # get select box value
    getCity = request.GET.get('city')
    
    # set select box value
    store = Store.objects.filter(str_city=getCity).values('str_name').order_by('str_city')
    
    return JsonResponse({'data': list(store)})