from django.urls import path
from app2.views import *
app_name='rohit'
urlpatterns=[
    path('india/',india,name='india'),
]