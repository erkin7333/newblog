from django import template
from main.models import Category

register = template.Library()



@register.simple_tag(name="cats")
def all_category():
    cats = Category.objects.all()
    return {'cats': cats}
