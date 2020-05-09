from django import template
from core.models import Order

register = template.Library()
'''
@register.filter
def cart_item_count(user)
'''


