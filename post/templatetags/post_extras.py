from django import template
from django.template.defaultfilters import stringfilter
import readtime
register = template.Library()

@register.filter
@stringfilter
def readTimeCount(value):
    result = readtime.of_text(value)
    return result.text 

@register.filter
@stringfilter
def activeState(value,arg):
    if value == arg:
        return 'active'
    return ''     




