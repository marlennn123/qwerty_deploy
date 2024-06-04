from django.urls import path
from .views import product_list, product_detail, product_create, product_update

urlpatterns = [
    path('', product_list, name='product_list'),
    path('<int:pk>/', product_detail, name='product_detail'),
    path('create/', product_create, name='product_create'),
    path('<int:pk>/update/', product_update, name='product_update'),
]