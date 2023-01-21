from django.urls import path
from .views import *


app_name = 'main'

urlpatterns = [
    path('', index, name='home'),

    path('detail/<int:pk>/', postdetaile, name='detail')
]