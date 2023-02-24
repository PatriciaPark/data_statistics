# from django import template
# from ..models import Dashboard_Table_month_basic
# from datetime import datetime

# #커스텀 태그: for문에서 제품 갯수만큼만 돌리기

# register = template.Library()

# # try:
# #     date = request.GET.get('input-month')   #2022-11
# #     year = date[:4]     #2022
# #     month = date[5:]    #11
# # except TypeError:
# #     year = datetime.today().year
# #     month = '1'

# #임시 -> 향후 위의 내용으로 수정
# year = datetime.today().year
# month = '1'

# @register.simple_tag
# def product_quantity(data):
#     data.