from django.shortcuts import render, redirect
from .models import New
from .forms import AddNewPost
from django.views.generic import ListView



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


def postdetaile(request, slug):
    details = New.objects.get(slug=slug)
    context = {
        'details': details
    }
    return render(request, 'main/postdetail.html', context=context)


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