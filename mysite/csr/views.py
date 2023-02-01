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
    # 지역만 선택
    if getloc != 'all' and (getCity is None or getCity == 'all') and (getStore is None or getStore == 'all'):
        data = StoreReview.objects.filter(str_code__str_loc=getloc).select_related('str_code').values('str_code__str_loc','str_code__str_city','str_code__str_name','str_img','str_comm','str_rate','user_id__username','str_date').order_by('-str_date')
    # 지역 및 시까지 선택
    elif getloc != 'all' and getCity is not None and (getStore is None or getStore == 'all'):
        data = StoreReview.objects.filter(str_code__str_loc=getloc, str_code__str_city=getCity).select_related('str_code').values('str_code__str_loc','str_code__str_city','str_code__str_name','str_img','str_comm','str_rate','user_id__username','str_date').order_by('-str_date')
    #지역, 시, 매장 선택
    elif getloc != 'all' and getCity is not None and getStore is not None:
        data = StoreReview.objects.filter(str_code__str_loc=getloc, str_code__str_city=getCity, str_code__str_name=getStore).select_related('str_code').values('str_code__str_loc','str_code__str_city','str_code__str_name','str_img','str_comm','str_rate','user_id__username','str_date').order_by('-str_date')
    else:
        data = StoreReview.objects.select_related('str_code').values('str_code__str_loc','str_code__str_city','str_code__str_name','str_img','str_comm','str_rate','user_id__username','str_date').order_by('-str_date')
    
    context = {'loc':loc, 'city':city, 'str':str, 'data':data}
    
    return render(request, 'csr/index.html', context)

# Create store review
def create(request):
    # get select box value
    getStrCode = request.POST.get('add-str')
    getComm = request.POST.get('add-comm')
    getRate = request.POST.get('add_rate')
    getImg = request.FILES.get('add_img')
    getUser = request.user
    
    user = User.objects.get(username = getUser)
    store = Store.objects.get(str_code = getStrCode)
    # Review 데이터 DB insert
    obj = StoreReview.objects.create(
        str_img = getImg,
        str_comm = getComm,
        str_rate = getRate,
        user_id = user,
        str_code = store
    )
    obj.save()
    
    print('**Inserted**', obj)
    
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
    store = Store.objects.filter(str_city=getCity).values('str_name','str_code').order_by('str_city')
    
    return JsonResponse({'data': list(store)})