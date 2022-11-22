from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    prd_code = models.CharField(help_text="Product code", max_length=200, primary_key=True)
    prd_barcode = models.CharField(max_length=200,null=False, blank=False)
    prd_name = models.CharField(max_length=200, null=False, blank=False)
    
    def __str__(self):
        return self.prd_name
    
    class Meta:
        db_table = 'tbl_product'
        verbose_name = 'Product Master'
        verbose_name_plural = 'Product Master'

    objects = models.Manager()

class Store(models.Model):
    str_code = models.CharField(help_text="store code", max_length=200, primary_key=True)
    str_city = models.CharField(max_length=200, null=False, blank=False)
    str_loc = models.CharField(help_text="store location",max_length=200)
    str_name = models.CharField(max_length=200, null=False, blank=False)

    def __str__(self):
        return (self.str_loc + "// " + self.str_city + "// " + self.str_name )

    class Meta:
        db_table = 'tbl_store'
        verbose_name = 'Store Master'
        verbose_name_plural = 'Store Master'

    objects = models.Manager()

class InvoiceDaily(models.Model):
    try:
        inv_d_code = models.BigAutoField(primary_key=True)
        inv_d_date = models.DateField( null=False, blank=False)
        inv_d_save = models.IntegerField(null=False, blank=False)
        inv_d_buy = models.IntegerField(null=False, blank=False)
        inv_d_return = models.IntegerField(null=False, blank=False)
        inv_d_sale = models.IntegerField(null=False, blank=False)
        inv_d_stock = models.IntegerField(null=False, blank=False)
        prd_code = models.ForeignKey(Product, null=True, on_delete = models.SET_NULL)
        str_code = models.ForeignKey(Store, null=True, on_delete = models.SET_NULL)
    except models.DoesNotExist :
        tbl_product = None

    def __str__(self):
        return (str(self.inv_d_date)+ ", "+ self.str_code.str_name + ", "+ self.prd_code.prd_name+ ", "+ str(self.prd_code.prd_barcode) +", "+ str(self.prd_code.prd_code))

    class Meta:
        db_table = 'tbl_invoice_d'
        verbose_name = 'Daily Invoice Master'
        verbose_name_plural = 'Daily Invoice Master'

    objects = models.Manager()
    
class DataDaily(models.Model):
    data_code = models.BigAutoField(primary_key=True)
    register_date = models.DateTimeField(auto_now_add = True)
    updated_date = models.DateTimeField(auto_now=True)
    data_path = models.FileField(upload_to='files/%Y%m%d/')
    data_name = models.CharField(max_length = 200)
    user_id = models.ForeignKey(User, on_delete = models.CASCADE)
    prd_code = models.ForeignKey(Product, null=True, on_delete = models.SET_NULL)
    str_code = models.ForeignKey(Store, null=True, on_delete = models.SET_NULL)

    def __str__(self):
        return f'[{self.data_name}] [{self.user_id}] [updated at: {self.updated_date}]'

    class Meta:
        db_table = 'tbl_data_d'
        verbose_name = 'Daily Data Master'
        verbose_name_plural = 'Daily Data Master'
        
# class SumDaily(models.Model):
#     sum_d_code = models.BigAutoField(primary_key=True)
#     sum_d_date = models.DateField( null=False, blank=False)
#     sum_d_save = models.IntegerField(null=False, blank=False)
#     sum_d_buy = models.IntegerField(null=False, blank=False)
#     sum_d_return = models.IntegerField(null=False, blank=False)
#     sum_d_sale = models.IntegerField(null=False, blank=False)
#     sum_d_stock = models.IntegerField(null=False, blank=False)
#     prd_code = models.ForeignKey(Product, null=True, on_delete = models.SET_NULL)
#     str_code = models.ForeignKey(Store, null=True, on_delete = models.SET_NULL) 
    
#     def __str__(self):
#         return (str(self.sum_d_date)+ ", "+ self.str_code.str_name + ", "+ self.prd_code.prd_name+ ", "+ str(self.prd_code.prd_barcode) +", "+ str(self.prd_code.prd_code))

#     class Meta:
#         db_table = 'tbl_sum_d'
#         verbose_name = 'Daily Sum Data'
#         verbose_name_plural = 'Daily Sum Data'
