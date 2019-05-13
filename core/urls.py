# Django
from django.contrib import admin
from django.urls import path,include

# 3rd partu swagger for docs
from rest_framework_swagger.views import get_swagger_view
from rest_framework.documentation import include_docs_urls

schema_view = get_swagger_view(title='Point of Sales API')

urlpatterns = [
    path('docs/',include_docs_urls(title="POS_API Documentation")),
    path('items/',include('core.items.urls')),
]