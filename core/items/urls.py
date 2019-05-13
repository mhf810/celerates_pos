# Django
from django.urls import path,include

# rest framework
from rest_framework.routers import DefaultRouter

# local : . menunjukkan direktori sekarang
from . import controllers

router = DefaultRouter()
router.register('',controllers.ItemController, basename='')

urlpatterns = [
    path('',include(router.urls))
]