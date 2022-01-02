# 自作フィルタの定義

from django import template

register = template.Library()

@register.filter
def TimeToCPS(time):
  # return 'a'
  return f'{360 / time:.3f}'