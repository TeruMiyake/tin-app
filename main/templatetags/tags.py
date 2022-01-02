# 自作フィルタの定義

from django import template

register = template.Library()

@register.filter
def TimeToCPS(time):
  # return 'a'
  if time != 0:
    return f'{360 / time:.3f}'
  else:
    return 0