from django.db import models
from django.contrib.auth.models import User, AbstractUser

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    availability = models.BooleanField(default=True)
    discount = models.DecimalField(max_digits=5, decimal_places=2, default=0)

    def is_available(self):
        return self.availability
        
    def __str__(self):
        return self.name

    def discounted_price(self):
        return self.price * (1 - self.discount / 100)

    @classmethod
    def get_discounted_products(cls):
        return cls.objects.filter(discount__gt=0)            

class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through='CartItem')

    def __str__(self):
        return f"Cart for {self.user.username}"

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through='OrderItem')
    created_at = models.DateTimeField(auto_now_add=True)

    def total_amount(self):
        total = sum(product.discounted_price() for product in self.products.all())
        return total

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

class User(AbstractUser):
    pass 

User._meta.get_field('groups').remote_field.related_name = 'user_groups' 
User._meta.get_field('user_permissions').remote_field.related_name = 'user_user_permissions'      



