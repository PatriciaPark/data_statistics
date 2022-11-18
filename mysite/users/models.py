from django.db import models

# Create your models here.
class User(models.Model):
    user_id = models.CharField(max_length=32, unique=True)
    user_pw = models.CharField(max_length=128)
    user_name = models.CharField(max_length=16, unique=True)
    user_email = models.EmailField(max_length=128, unique=True)
    user_reg_date = models.DateTimeField(auto_now_add=True)
    
    # 생성된 객체의 이름을 지정하는 메서드. 
    # 이것을 등록하지 않으면 User 클래스로 생성된 object 불러왔을때 User object(1) 이런식으로 리턴
    def __str__(self):
        return self.user_name
    
    # 테이블명 지정 옵션 : 테이블명/닉네임/닉네임2
    class Meta:
        db_table = 'tbl_user'
        verbose_name = 'User Master'
        verbose_name_plural = 'User Master'