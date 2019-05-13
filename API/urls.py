# Django
from django.contrib import admin
from django.urls import path,include

# local
from core import views

urlpatterns = [
    # list of PATH API Object  
    path('',include('core.urls'))
]