import imp
from itertools import product
from django.contrib import admin
from Home.models import Category,Product,Customer,orders
# Register your models here.
class product(admin.ModelAdmin):
    list_display=["name","price","description","category"]

class customer(admin.ModelAdmin):
    list_display=["name","email","phone","password"]    
class order(admin.ModelAdmin):
    list_display=["customer","phone","product","price"]      
admin.site.register(Product,product)
admin.site.register(Category)
admin.site.register(Customer,customer)
admin.site.register(orders,order)
