from django.shortcuts import render
from csd.models import Product

# Create your views here.
# index
def index(request):
    # html에서 선택한 select box value 받아오기 및 정렬
    sort    = request.GET.get('input-sort') #정렬
    
    if sort == 'prdcode':
        data = Product.objects.all().order_by('prd_code')
    elif sort == 'prdbarcode':
        data = Product.objects.all().order_by('prd_barcode')
    elif sort == 'prdname':    
        data = Product.objects.all().order_by('prd_name')
    else:
        data = Product.objects.all().order_by('prd_code')
    
    
    context = {'data':data, 'sort':sort}
    
    return render(request, 'product/index.html', context)