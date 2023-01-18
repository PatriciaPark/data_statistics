from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from csd.models import Store

# Index(main)
def index(request):
    
    # get select box value
    getloc = request.GET.get('input-loc')
    getCity = request.GET.get('input-city')
    
    print('getloc: ',getloc, ', getCity:', getCity)
    
    # set select box value
    loc = Store.objects.values('str_loc').distinct()
    city = Store.objects.filter(str_loc=getloc).values('str_city').distinct().order_by('str_city')
    
    # read data
    if getloc == 'all':
        data = Store.objects.all().order_by('str_city')
    elif getloc is not None and (getCity is None or getCity == 'all'):
        data = Store.objects.filter(str_loc=getloc).all().order_by('str_city')
    elif getloc is not None and getCity is not None:
        data = Store.objects.filter(str_loc=getloc, str_city=getCity).all().order_by('str_city')
    else:
        data = Store.objects.all().order_by('str_city')
    
    context = {'loc':loc, 'city':city, 'data':data}
    
    return render(request, 'store/index.html', context)

# Store Info Field Update
def update(request):
    
    # get select box value
    getloc = request.POST.get('info-loc')
    getCity = request.POST.get('info-city')
    getCode = request.POST.get('info-code')
    
    print('Location:', getloc, ', City:', getCity, ', Code:', getCode)
    # 매장 데이터 DB update
    obj = Store.objects.filter(str_code=getCode).update(str_loc=getloc, str_city=getCity)
    
    print('**Updated**', obj)
    
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

# Store Info Field Select Box
def select(request):
    
    # get select box value
    getloc = request.GET.get('location')
    
    # set select box value
    city = Store.objects.filter(str_loc=getloc).values('str_city').distinct().order_by('str_city')
    
    return JsonResponse({'data': list(city)})
