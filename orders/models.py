from django.db import models
from django.db import models
from django.conf import settings



class Order(models.Model):
    STATUS_CHOICES = (
        ('Pending', 'Kutilmoqda'),
        ('Confirmed', 'Tasdiqlandi'),
        ('Shipped', 'Yo\'lda'),
        ('Delivered', 'Yetkazildi'),
        ('Cancelled', 'Bekor qilindi'),
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey('products.Product', on_delete=models.SET_NULL, null=True)

    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)