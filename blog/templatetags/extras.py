#This is how we create custum filter(tamplate tag) in django templates
#make __init__.py in templatetag-----> declares extras.py as a package
from django import template

register=template.Library()

@register.filter(name='get_val')
def get_val(dict, key):
    return dict.get(key)  #or dict[key]