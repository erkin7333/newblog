from django.urls import path
from .views import *


app_name = 'main'

urlpatterns = [
    path('', NewsListView.as_view(), name='home'),

    path('category/<slug:slug>/', filternews, name='filtercat'),

    path('detail/<slug:slug>/', NewsDetailView.as_view(), name='detail'),

    path('addnews/', addnews, name='addnews')
]