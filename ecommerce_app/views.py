from rest_framework import generics, permissions
from .models import Product, Cart, Order, User
from .serializer import ProductSerializer, CartSerializer, OrderSerializer, UserSerializer



class ProductList(generics.ListAPIView):
    queryset = Product.objects.filter(availability=True)
    serializer_class = ProductSerializer

class CartDetail(generics.RetrieveUpdateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user.cart

class OrderCreate(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        cart = self.request.user.cart
        products = cart.products.all()

        total_price = sum(product.price * item.quantity for product, item in zip(products, cart.cartitem_set.all()))
        serializer.save(user=self.request.user, products=products, total_price=total_price)
        cart.products.clear()

class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


    





