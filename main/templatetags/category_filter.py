from django import template
from main.models import Category

register = template.Library()



@register.simple_tag(name="categories")
def all_category():
    return Category.objects.all()
