from django.db import models
from csd.models import Product

# Create your models here.

class CommonInfo(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

class Product_selling_price(CommonInfo):
    product_id    = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL,)   #제품명
    selling_price = models.IntegerField()                                               #판매가, 자료기입
    year          = models.DateField()

    def __str__(self):
        return self.product_id.prd_name + "-" + "{}".format(self.year)

class Dashboard_Table_month_basic(CommonInfo):
    product_selling_price_id = models.ForeignKey(Product_selling_price, null=True, on_delete = models.SET_NULL) #제품명과 판매가
    date            = models.DateField()                            #당월 연, 월단위 날짜, day = 1로 세팅 <-sum_monthly의 db와 같다(이렇게 저장되어 있다.)
    target_qauntity = models.IntegerField(null=True, blank=True)    #당월 목표: 판매량, 자료 기입
    target_sales    = models.IntegerField(null=True, blank=True)    #당월 목표: 매출, 자료 기입
    expect_qauntity = models.IntegerField(null=True, blank=True)    #당월 전망:판매량, 자료 기입
    expect_sales    = models.IntegerField(null=True, blank=True)    #당월 전망: 매출, 자료 기입

    def __str__(self):
        return self.product_selling_price_id.product_id.prd_name + "-" + "{}".format(self.date)