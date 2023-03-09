from django.shortcuts import render
from csd.models import Product

# Create your views here.
# index
def index(request):
    
    data = Product.objects.all().order_by('prd_code')
    
    context = {'data':data}
    
    return render(request, 'product/index.html', context)