from django.shortcuts import render, redirect
from .models import New
from .forms import AddNewPost
from django.views.generic import ListView, DetailView



def index(request):
    """Yangiliklarni chiqarish uchun funksiya"""

    posts = New.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'main/index.html', context=context)


class NewsListView(ListView):
    """Yangiliklarni chiqarish uchun Class based views"""

    model = New
    template_name = 'main/index.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return New.objects.filter(is_published=True)


def postdetaile(request, slug):
    """Yangiliklarni tavsilotni ko'rish uchun funksiya"""

    details = New.objects.get(slug=slug)
    context = {
        'details': details
    }
    return render(request, 'main/postdetail.html', context=context)


class NewsDetailView(DetailView):
    """Yangiliklarni tavsilotlarini chiqarish uchun Class based views"""

    model = New
    template_name = "main/postdetail.html"
    context_object_name = "details"

    def get_queryset(self):
        return New.objects.filter(slug=self.kwargs['slug'], is_published=True)


def addnews(request):
    if request.method == 'POST':
        form = AddNewPost(request.POST, request.FILES)
        if form.is_valid():
            try:
                form.save()
                return redirect('main:home')
            except:
                form.add_error(None, "Malumot yuklashda xatolik yuzaga keldi")
    else:
        form = AddNewPost()
    return render(request, 'main/addnews.html', {'form': form})


def filternews(request, slug):
    """Yangiliklarni kategoriyalari bo'yicha filterlash"""

    newfilter = New.objects.filter(cat__slug=slug)
    context = {
        'newfilter': newfilter
    }
    return render(request, 'main/filtercategory.html', context=context)