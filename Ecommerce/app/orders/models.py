from django.db import models
from app.customer.models import customers
from app.product.models import products_table

# Create your models here.
class order(models.Model):
    LIVE = 1
    DELETE = 0
    DELETE_CHOICE = ((LIVE,'Live'),(DELETE,'Delete'))
    CART_STAGE = 0
    ORDER_CONFIRMED = 1
    ORDER_PROCESSED = 2
    ORDER_DELIVERED = 3
    ORDER_REJECTED = 4
    STATUS_CHOICE = ((ORDER_CONFIRMED,'ORDER_CONFIRMED'),
                     (ORDER_PROCESSED,'ORDER_PROCESSED'),
                     (ORDER_DELIVERED,'ORDER_DELIVERED'),
                     (ORDER_REJECTED,'ORDER_REJECTED'))
    order_status = models.IntegerField(choices=STATUS_CHOICE,default=CART_STAGE)
    owner = models.ForeignKey(customers,on_delete=models.SET_NULL,null=True,related_name='orderd_item')
    deleted_status = models.IntegerField(choices=DELETE_CHOICE,default=DELETE)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    """def __str__(self):
        return  {self.owner.name}"""

class order_items(models.Model):
    product = models.ForeignKey(products_table,related_name='added_cart',on_delete=models.SET_NULL,null=True)
    quantity = models.IntegerField(default=1)
    owner = models.ForeignKey(order,on_delete=models.CASCADE,null=True,related_name='added_items')

    """def __str__(self) -> str:
         
         return f" ID: {self.owner.id} - Customer: {self.owner.owner.name}"""