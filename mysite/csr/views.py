from django.shortcuts import render
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
    
    
    
    context = {'loc':loc, 'city':city, 'str':str}
    
    return render(request, 'csr/index.html', context)