from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class product (models.Model):
    name=models.CharField(max_length=50)
    image=models.FileField(upload_to='product_images/',null=True,blank=True)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    quantity=models.TextField()
    description=models.TextField()
    def __str__(self)->str:
        return self.name 
    
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product=models.ForeignKey('product',on_delete=models.CASCADE)
    quantity=models.PositiveBigIntegerField(default=1)

    def __str__(self) ->str:
        return f"Cart for {self.user.username}"
    def line_total(self):
        return self.quantity*self.product.price 
    
class Order(models.Model):
    STATUS_CHOICES=[
        ('Pending','Pending'),
        ('Delivered','Delivered'),
        ('Cancelled','Cancelled'),
    ]  
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=225)
    address= models.CharField(max_length=165)
    phone_number=models.CharField(max_length=15)
    total_order_price=models.DecimalField(max_digits=10,decimal_places=2,default=0)
    status=models.CharField(choices=STATUS_CHOICES,default="Pending",max_length=225)

    def __str__(self)->str:
        return f"Order #{self.id}by {self.user.username}" 
    
    def update_total_order_price(self):
        total_price=sum(detail.total_price for detail in self.orderdetail_set.all())
        self.total_order_price=total_price
        self.save()

class OrderDetail(models.Model):
    order=models.ForeignKey(Order,on_delete=models.CASCADE)
    product=models.ForeignKey(product,on_delete=models.CASCADE)
    quantity=models.PositiveBigIntegerField()
    unit_price=models.DecimalField(max_digits=10,decimal_places=2)
    total_price=models.DecimalField(max_digits=10,decimal_places=2)

    def save(self,*args,**kwargs):
        self.total_price=self.unit_price*self.quantity
        super().save(*args,**kwargs)
        self.order.update_total_order_price()

class WishList(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey('product',on_delete=models.CASCADE)
    quantity=models.PositiveBigIntegerField(default=1)

    def __str__(self) ->str:
        return f'{self.user.username} added wishlist'
    
class Profile(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    image=models.FileField(upload_to='profile_images/',null=True,blank=True)
      




    
    
 
