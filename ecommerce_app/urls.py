from django.urls import path
from .views import ProductList, CartDetail, OrderCreate, UserCreate, DiscountedProductView, ProductAvailabilityView
from . import views

urlpatterns = [
    path('products/', ProductList.as_view(), name='product-list'),
    path('cart/', CartDetail.as_view(), name='cart-detail'),
    path('orders/create/', OrderCreate.as_view(), name='order-create'),
    path('users/register/', UserCreate.as_view(), name='user-create'),
    path('discounted-products/', DiscountedProductView.as_view(), name='discounted_products'),
    path('product-availability/', ProductAvailabilityView.as_view(), name='product_availability'),
]
