from django import template


register = template.Library()

@register.filter(name='filter_by_status')
def filter_by_status(shipments, status):
    return shipments.filter(status=status)