from django.db import models
from django.contrib.auth.models import User
from csd.models import Product, Store

# 데이터 테이블    
class DataMonthly(models.Model):
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
        db_table = 'tbl_data_m'
        verbose_name = 'Monthly Data Master'
        verbose_name_plural = 'Monthly Data Master'

# 합계 테이블 (monthly)
class SumMonthly(models.Model):
    sum_m_code = models.BigAutoField(primary_key=True)
    sum_m_date = models.DateField( null=False, blank=False)
    sum_m_save = models.IntegerField(null=False, blank=False)
    sum_m_buy = models.IntegerField(null=False, blank=False)
    sum_m_return = models.IntegerField(null=False, blank=False)
    sum_m_sale = models.IntegerField(null=False, blank=False)
    sum_m_stock = models.IntegerField(null=False, blank=False)
    sum_m_sale_ttl = models.FloatField(null=True, blank=True)
    sum_m_sale_err = models.FloatField(null=True, blank=True)
    sum_m_stock_mon = models.FloatField(null=True, blank=True)
    prd_code = models.ForeignKey(Product, null=True, on_delete = models.SET_NULL)
    str_code = models.ForeignKey(Store, null=True, on_delete = models.SET_NULL)
    
    def __str__(self):
        return "%s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s" % (self.sum_m_date, self.str_code.str_loc, self.str_code.str_city, self.str_code.str_code, 
                                                           self.str_code.str_name, self.prd_code.prd_code, self.prd_code.prd_name, self.prd_code.prd_barcode, 
                                                           self.sum_m_save, self.sum_m_buy, self.sum_m_return, self.sum_m_sale, self.sum_m_stock,
                                                           self.sum_m_sale_ttl, self.sum_m_sale_err, self.sum_m_stock_mon)

    class Meta:
        db_table = 'tbl_sum_m'
        verbose_name = 'Monthly Sum Data'
        verbose_name_plural = 'Monthly Sum Data'
        
    objects = models.Manager()