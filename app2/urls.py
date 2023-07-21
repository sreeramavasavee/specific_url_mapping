from django.urls import path
from app2.views import *
app2_name='two'
urlpatterns=[
    path('first/',first,name='first'),
    path('second/',second,name='second'),
]
