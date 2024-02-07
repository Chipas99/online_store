from django.urls import path

from catalog.views import contacts, product_detail

urlpatterns = [
    path('', product_detail),
    path('contacts/', contacts)
]
