from django import template
register = template.Library()

@register.filter
def index(indexable, i):
    try:
        return indexable[i]
    except:
        return None
    
@register.filter
def div(value, div):
    if div == 0:
        return 0
    return round((value / div) * 100 / 100, 2)