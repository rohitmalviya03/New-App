import imp
from itertools import product
from django.contrib import admin
from Home.models import Category,Product,Customer
# Register your models here.
class product(admin.ModelAdmin):
    list_display=["name","price","description","category"]

class customer(admin.ModelAdmin):
    list_display=["name","email","phone","password"]    
admin.site.register(Product,product)
admin.site.register(Category)
admin.site.register(Customer,customer)
