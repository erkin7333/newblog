from django.shortcuts import render
from .models import New


def index(request):
    posts = New.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'main/index.html', context=context)


def postdetaile(request, pk):
    details = New.objects.filter(id=pk)
    context = {
        'details': details
    }
    return render(request, 'main/postdetail.html', context=context)
