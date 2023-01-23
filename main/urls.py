from django.urls import path
from .views import *


app_name = 'main'

urlpatterns = [
    path('', NewsListView.as_view(), name='home'),

    path('detail/<slug:slug>/', postdetaile, name='detail'),

    path('addnews/', addnews, name='addnews')
]