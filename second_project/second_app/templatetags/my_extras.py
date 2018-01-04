from django import template

register = template.Library()

@register.filter(name = 'cut')
def cut(value, arg):
    """
    This cuts out all values of "args" from the string!
    """
    return value.replace(arg, '')

#normal way to register
#register.filter('cut', )

#use decorator to do register
