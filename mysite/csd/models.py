from django.db import models
from django.contrib.auth.models import User

# 상품테이블
class Product(models.Model):
    prd_code = models.CharField(help_text="Product code", max_length=200, primary_key=True)
    prd_barcode = models.CharField(max_length=200,null=False, blank=False)
    prd_name = models.CharField(max_length=200, null=False, blank=False)
    
    def __str__(self):
        return (self.prd_name + ", " + self.prd_barcode + ", " + self.prd_code)
    
    class Meta:
        db_table = 'tbl_product'
        verbose_name = 'Product Master'
        verbose_name_plural = 'Product Master'

    objects = models.Manager()
    
# 매장테이블
class Store(models.Model):
    str_code = models.CharField(help_text="store code", max_length=200, primary_key=True)
    str_city = models.CharField(max_length=200)
    str_loc = models.CharField(help_text="store location",max_length=200)
    str_name = models.CharField(max_length=200, null=False, blank=False)

    def __str__(self):
        return "%s %s %s %s" % (self.str_code, self.str_loc, self.str_city, self.str_name )

    class Meta:
        db_table = 'tbl_store'
        verbose_name = 'Store Master'
        verbose_name_plural = 'Store Master'

    objects = models.Manager()
    
# 주문테이블(데일리)
class InvoiceDaily(models.Model):
    inv_d_code = models.BigAutoField(primary_key=True)
    inv_d_date = models.DateField( null=False, blank=False)
    inv_d_save = models.IntegerField(null=True, blank=True)
    inv_d_buy = models.IntegerField(null=True, blank=True)
    inv_d_return = models.IntegerField(null=True, blank=True)
    inv_d_sale = models.IntegerField(null=True, blank=True)
    inv_d_stock = models.IntegerField(null=True, blank=True)
    prd_code = models.ForeignKey(Product, null=True, on_delete = models.SET_NULL)
    str_code = models.ForeignKey(Store, null=True, on_delete = models.SET_NULL)

    def __str__(self):
        return "%s %s %s %s %s %s %s %s %s %s %s" % (self.inv_d_date, self.prd_code, self.prd_code.prd_name,
                                            self.str_code, self.str_code.str_name, self.str_code.str_city,
                                            self.inv_d_save, self.inv_d_buy, self.inv_d_return, self.inv_d_sale, self.inv_d_stock)

    class Meta:
        db_table = 'tbl_invoice_d'
        verbose_name = 'Daily Invoice Master'
        verbose_name_plural = 'Daily Invoice Master'

    objects = models.Manager()

# 주문테이블(데일리의 마지막 일자 데이터 = 그 달의 데이터 합)
class InvoiceMonthly(models.Model):
    inv_m_code = models.BigAutoField(primary_key=True)
    inv_m_date = models.DateField( null=False, blank=False)
    inv_m_save = models.IntegerField(null=True, blank=True)
    inv_m_buy = models.IntegerField(null=True, blank=True)
    inv_m_return = models.IntegerField(null=True, blank=True)
    inv_m_sale = models.IntegerField(null=True, blank=True)
    inv_m_stock = models.IntegerField(null=True, blank=True)
    prd_code = models.ForeignKey(Product, null=True, on_delete = models.SET_NULL)
    str_code = models.ForeignKey(Store, null=True, on_delete = models.SET_NULL)

    def __str__(self):
        return "%s %s %s %s %s %s %s %s %s %s %s" % (self.inv_m_date, self.prd_code, self.prd_code.prd_name,
                                            self.str_code, self.str_code.str_name, self.str_code.str_city,
                                            self.inv_m_save, self.inv_m_buy, self.inv_m_return, self.inv_m_sale, self.inv_m_stock)

    class Meta:
        db_table = 'tbl_invoice_m'
        verbose_name = 'Monthly Invoice Master'
        verbose_name_plural = 'Monthly Invoice Master'

    objects = models.Manager()

# 합계 테이블 (데일리)
class SumDaily(models.Model):
    sum_d_code = models.BigAutoField(primary_key=True)
    sum_d_date = models.DateField(null=False, blank=False)
    sum_d_save = models.IntegerField(null=False, blank=False)
    sum_d_buy = models.IntegerField(null=False, blank=False)
    sum_d_return = models.IntegerField(null=False, blank=False)
    sum_d_sale = models.IntegerField(null=False, blank=False)
    sum_d_stock = models.IntegerField(null=False, blank=False)
    prd_code = models.ForeignKey(Product, null=True, on_delete = models.SET_NULL)
    # str_code = models.ForeignKey(Store, null=True, on_delete = models.SET_NULL) 
    
    def __str__(self):
        return (str(self.sum_d_date)+ ", "+ self.prd_code.prd_name+ ", "+ str(self.prd_code.prd_barcode) +", "+ str(self.prd_code.prd_code) + "," + str(self.sum_d_sale))

    class Meta:
        db_table = 'tbl_sum_d'
        verbose_name = 'Daily Sum Data'
        verbose_name_plural = 'Daily Sum Data'