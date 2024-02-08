from django.urls import path
from catalog import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contacts/', views.contacts),
    path('product/<int:pk>/', views.product_detail),
]
