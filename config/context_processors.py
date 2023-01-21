from main.models import Category


def all_category(request):
    cats = Category.objects.all()
    return {'cats': cats}