from django.contrib import admin
from django.urls import path

from covid_info import views

urlpatterns = [
    path('',views.index,name='index'),
]
