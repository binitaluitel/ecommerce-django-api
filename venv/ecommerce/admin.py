from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(product)
class productAdmin(admin.ModelAdmin):
    list_display=['name','price','image','quantity','description']

admin.site.register(Cart)

class OrderDetailInline(admin.TabularInline):
    model= OrderDetail
    extra= 1
    readonly_fields=('product','quantity','unit_price','total_price')

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
      inlines=[OrderDetailInline]
      readonly_fields = ('name','total_order_price','user')
      list_display=['name','total_order_price','status']

admin.site.register(WishList)

admin.site.register(Profile)




