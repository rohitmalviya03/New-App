from statistics import mode
from unicodedata import category
from django.db import models
from django.forms import IntegerField


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
    
   