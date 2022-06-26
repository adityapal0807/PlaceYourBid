from django.contrib import admin
from .models import Item,User,Wishlist,Comments,Bid
# Register your models here.

admin.site.register(Item)
admin.site.register(User)
admin.site.register(Wishlist)
admin.site.register(Comments)
admin.site.register(Bid)
