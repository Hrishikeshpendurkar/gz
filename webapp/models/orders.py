from email.headerregistry import Address
from email.policy import default
from django.db import models
from datetime import datetime
from .product_info import Product
from .user_info import User_data


class Order(models.Model):
    product = models.ForeignKey(Product,on_delete = models.CASCADE)
    customer = models.ForeignKey(User_data,on_delete = models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.CharField(max_length=10, default='')
    address = models.CharField(max_length=100, default='', blank=True, null=True)
    phone = models.CharField(max_length=15, default='', blank=True, null=True)
    date = models.DateTimeField( default=datetime.now())
    status = models.BooleanField( default=False)

    def __str__(self) -> str:
         return self.customer.Email
        
    def placeOrder(self):
        self.save()
    
    @staticmethod
    def get_orders_by_customer(customer_id):
        return Order\
            .objects\
            .filter(customer = customer_id).order_by('-date')