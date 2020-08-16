from django import template
register = template.Library()

@register.filter(name="getData")
def getData(dict, key_parent):
    return dict.get(key_parent)
    
