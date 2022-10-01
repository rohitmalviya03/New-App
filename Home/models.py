from datetime import datetime
from itertools import product
from statistics import mode
from unicodedata import category
from django.db import models
from django.forms import IntegerField
import datetime


# Create your models here.

class Category(models.Model):
       Name = models.CharField(max_length=50)
       @staticmethod
       def get_all_categories():
            return Category.objects.all()
       def __str__(self):
            return self.Name

class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    description = models.CharField(max_length=200, default='' , null=True , blank=True)
    image = models.ImageField(upload_to='uploads/products/')
    

    @staticmethod
    def get_product_by_id(ids):
        return Product.objects.filter(id__in=ids)

    @staticmethod
    def getallproducts():
        return Product.objects.all()
    @staticmethod
    def get_all_products():
        return Product.objects.all()

    
     
    @staticmethod
    def get_all_products_by_categoryid(category_id):
        if category_id:
            return Product.objects.filter(category = category_id)
        else:
            return Product.get_all_products();  

class Customer(models.Model):
    
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    password = models.CharField(max_length=500) 



    # def __str__(self):
    #         return self.email
    def isExists(uemail):
        if Customer.objects.filter(email = uemail):
            return True
        else: 
           return False


    @staticmethod
    def get_customer(email):
        try:
            return Customer.objects.get(email=email)
        except:
            return False  

class orders(models.Model):
    customer =models.ForeignKey(Customer,max_length=50,on_delete=models.CASCADE,)
    phone=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    price=models.CharField(max_length=50,default=0)
    date=models.DateField(default=datetime.datetime.today)
    quantity =models.IntegerField(default=0)
  
    product =models.ForeignKey(Product,max_length=50,on_delete=models.CASCADE,)

    @staticmethod
    def get_order_by_customer(customer_id):
        return orders.objects.filter(customer=customer_id).order_by('-date')    # def placeOrder(self):
    #     return self.save
      