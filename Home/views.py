import imp
from itertools import product
from unicodedata import category
from django.shortcuts import render
from Home.models import Category,Product
from django.views import View
from django.shortcuts import render , redirect , HttpResponseRedirect

# Create your views here.

def index(request):
    products=Product.getallproducts()
    print(products)
    categories = Category.get_all_categories()
    categoryID = request.GET.get('category')
    print(categoryID)
    if categoryID:
        products = Product.get_all_products_by_categoryid(categoryID)
    else:
        products = Product.get_all_products()
    data = {}
    data['products'] = products
    data['categories'] = categories
 
    return render(request,"index.html",data)
    
def showdata(request):
    products = Product.objects.all() 
    
    return render(request,'showdata.html',{'products':products})

# print("Cat",Product.objects.filter(category = 3))
       