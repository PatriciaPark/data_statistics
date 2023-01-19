from django.db import models
from django.contrib.auth.models import User
from csd.models import Store

# 매장 리뷰 테이블
class StoreReview(models.Model):
    str_rcode = models.BigAutoField(primary_key=True)
    str_img = models.ImageField(upload_to='media/%Y/%m/%d/', height_field=None, width_field=None, max_length=100)
    str_comm = models.CharField(max_length=500, null=False, blank=False)
    str_rate = models.IntegerField(null=True, blank=True)
    str_date = models.DateTimeField(auto_now_add = True)
    user_id = models.ForeignKey(User, on_delete = models.CASCADE)
    str_code = models.ForeignKey(Store, null=True, on_delete = models.SET_NULL)

    def __str__(self):
        return "%s %s %s %s %s %s %s %s %s %s" % (self.str_rcode, self.str_img, self.str_comm, 
                                               self.str_rate, self.str_date, self.user_id, self.str_code,
                                               self.str_code.str_loc, self.str_code.str_city, self.str_code.str_name)

    class Meta:
        db_table = 'tbl_str_review'
        verbose_name = 'Store Review Data'
        verbose_name_plural = 'Store Review Data'
        
    objects = models.Manager()