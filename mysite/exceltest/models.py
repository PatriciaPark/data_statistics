from django.db import models
from django.contrib.auth.models import User
from distutils.command.upload import upload

# class SampleModel(models.Model): 
#     Name = models.CharField(max_length = 10, null = False)
#     Number = models.IntegerField(null = True)
#     Item = models.CharField(max_length = 10, null = True)

class Document(models.Model):
    file_id = models.BigAutoField(primary_key=True)
    file_path = models.FileField(upload_to='upload_files/%Y%m%d/')
    file_name = models.CharField(max_length = 200)
    file_user = models.ForeignKey(User, on_delete = models.CASCADE)
    file_create_time = models.DateTimeField(auto_now_add = True)
    file_updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'[{self.file_name}] [{self.file_user}] [updated at: {self.file_updated_at}]'

    class Meta:
        verbose_name_plural = 'documents_uploaded'

class tbl_product(models.Model):
    product_code = models.CharField(help_text="Product code", max_length=200,primary_key=True)
    product_code_bystore = models.CharField(help_text="Product store code", max_length=200)
    product_barcode = models.CharField(max_length=200,null=False, blank=False)
    product_name = models.CharField(max_length=200, null=False, blank=False)
    product_detail = models.TextField(null=False, blank=False)
    product_use = models.BooleanField(default=True)
    product_create_time = models.DateTimeField(auto_now_add = True)
    product_updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product_name
    
    class Meta:
        verbose_name_plural = 'product_master_data'

    objects = models.Manager()

class tbl_store(models.Model):
    store_code = models.CharField(help_text="store code", max_length=200,primary_key=True)
    store_name = models.CharField(max_length=200, null=False, blank=False)
    store_district = models.CharField(max_length=200,null=False, blank=False)
    store_city = models.CharField(max_length=200, null=False, blank=False)
    store_address = models.TextField(null=False, blank=False)
    store_detail = models.TextField(null=True, blank=True)
    store_start = models.DateField(null=False, blank=False)
    store_end = models.DateField(null=True, blank=True)
    store_use = models.BooleanField(default=True)
    store_create_time = models.DateTimeField(auto_now_add = True)
    store_updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return (self.store_district + "// " + self.store_city + "// " + self.store_name )

    class Meta:
        verbose_name_plural = 'store_master_data'

    objects = models.Manager()

class tbl_invoice_daily(models.Model):
    invoice_day_id = models.BigAutoField(primary_key=True)
    invoice_day_date = models.DateField( null=False, blank=False)
    invoice_day_save = models.IntegerField(null=False, blank=False)
    invoice_day_buy = models.IntegerField(null=False, blank=False)
    invoice_day_return = models.IntegerField(null=False, blank=False)
    invoice_day_sale = models.IntegerField(null=False, blank=False)
    invoice_day_stock = models.IntegerField(null=False, blank=False)
    invoice_day_product = models.ForeignKey(tbl_product, null=True, on_delete = models.SET_NULL)
    invoice_day_store = models.ForeignKey(tbl_store, null=True, on_delete = models.SET_NULL)
    invoice_day_create_time = models.DateTimeField(auto_now_add = True)
    invoice_day_updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return (str(self.invoice_day_date)+ " // "+ self.invoice_day_store.store_name + " // "+ self.invoice_day_product.product_name )

    class Meta:
        verbose_name_plural = 'daily_row_data'

    objects = models.Manager()