from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import datetime


class User(AbstractUser):
    pass

class Item(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    seller = models.ForeignKey(User,on_delete=models.CASCADE)
    start_price = models.IntegerField()
    time = models.DateTimeField(default=datetime.now)
    photo = models.ImageField(default="images/noimage.jpg",upload_to='images')
    closed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title} , {self.closed}"


class Wishlist(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Item,on_delete=models.CASCADE)

class Comments(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Item,on_delete=models.CASCADE)
    comment = models.TextField(max_length=1000)

    def __str__(self):
        return f"{self.user} on {self.product}"

class Bid(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Item,on_delete=models.CASCADE)
    bid_amount = models.IntegerField()

    def __str__(self):
        return f"{self.user} placed {self.bid_amount} on {self.product}"


