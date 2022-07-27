import imp
from itertools import product
from django.contrib import admin
from Home.models import Category,Product
# Register your models here.
class product(admin.ModelAdmin):
    list_display=["name","price","description","category"]
admin.site.register(Product,product)
admin.site.register(Category)
