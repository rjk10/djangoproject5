from django.urls import path
from app1.views import *
app_name='indian'
urlpatterns=[
    path('india/',india,name='india'),
]