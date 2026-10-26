from django import template

register = template.Library()


@register.filter
def age_label(age):
    if age == 0:
        return 'под 1 година'
    elif age == 1:
        return f'{age} година'
    else: 
        return f'{age} години'