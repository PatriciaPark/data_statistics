from django.db import models
from csd.models import Product, SumDaily
from csm.models import DataMonthly, SumMonthly
from django.db.models import Q
import datetime

# Create your models here.

class CommonInfo(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

class Product_selling_price(CommonInfo):
    product_id = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL,)#제품명
    selling_price = models.IntegerField() #판매가, 자료기입
    year = models.DateField()

    def __str__(self):
        return self.product_id.prd_name + "-" + "{}".format(self.year)

class Dashboard_Table_month_basic(CommonInfo):
    product_selling_price_id = models.ForeignKey(Product_selling_price, null=True, on_delete = models.SET_NULL) #제품명과 판매가
    date = models.DateField() #당월 연, 월단위 날짜, day = 1로 세팅 <-sum_monthly의 db와 같다(이렇게 저장되어 있다.)
    target_qauntity = models.IntegerField(null=True, blank=True) #당월 목표: 판매량, 자료 기입
    target_sales = models.IntegerField(null=True, blank=True) #당월 목표: 매출, 자료 기입
    expect_qauntity = models.IntegerField(null=True, blank=True) #당월 전망:판매량, 자료 기입
    expect_sales = models.IntegerField(null=True, blank=True) #당월 전망: 매출, 자료 기입

    def __str__(self):
        return self.product_selling_price_id.product_id.prd_name + "-" + "{}".format(self.date)

    # #월_누적_판매량
    # @property
    # def accumulated_quantity(self):
    #     accumulated_quantity = SumDaily.objects.get(Q(prd_code=self.product_selling_price_id.product_id) & Q(sum_d_date= self.date))
    #     return accumulated_quantity.sum_d_sale

    # #월_누적_매출
    # @property
    # def accumulated_salse(self):
    #     product_selling_price = self.product_selling_price_id.selling_price
    #     accumulated_sales = self.accumulated_quantity * product_selling_price
    #     return accumulated_sales

    # #전년_동월_판매량
    # @property
    # def last_year_month_quantity(self):
    #     year = datetime.today().year
    #     month = datetime.today().strftime('%m')#임시 -> 나중에 검색할 수 있게 바꿔야 함
    #     # last_year_same_month = datetime.datetime(self.date.year-1,self.date.month, self.date.day)
    #     last_year_month_quantity = SumMonthly.objects.get(prd_code=self.product_selling_price_id.product_id, sum_m_date__year=(int(year)-1), sum_m_date__month=int(month))
    #     # last_year_month_quantity = SumMonthly.objects.get(Q(prd_code=self.product_selling_price_id.product_id) & Q(sum_d_date= last_year_same_month))
    #     return last_year_month_quantity

    # #전년_동월_매출
    # @property
    # def last_year_month_salse(self):
    #     year = datetime.today().year
    #     product_selling_price = Product_selling_price.objects.get(Q(product_selling_price_id=self.product_selling_price_id.product_id) & Q(year__year = (int(year)-1)))#1년전 month 매칭 해야함..
    #     last_year_month_sales = self.last_year_month_quantity * product_selling_price
    #     return last_year_month_sales

    # #금월_진도율_판매량
    # @property
    # def achievement_quantity(self):
    #     return self.accumulated_quantity / self.target_qauntity

    # #금월_진도율_매출
    # @property
    # def achievement_salse(self):
    #     return self.accumulated_salse / self.target_sales

    # #목표비_판매량
    # @property
    # def target_ratio_quantity(self):
    #     return self.expect_qauntity / self.target_qauntity

    # #목표비_매출
    # @property
    # def target_ratio_salse(self):
    #     return self.expect_sales / self.target_sales

    # #전년비_판매량
    # @property
    # def yoy_quantity(self):
    #     return self.expect_qauntity / self.last_year_month_quantity

    # #전년비_매출
    # @property
    # def yoy_salse(self):
    #     return self.expect_sales / self.last_year_month_salse



