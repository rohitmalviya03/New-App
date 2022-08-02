from distutils.log import error
import email
import imp
from itertools import product
from threading import currentThread
from unicodedata import category, name
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.hashers import make_password,check_password

from Home.models import Category,Product,Customer
from django.views import View
from django.shortcuts import render , redirect , HttpResponseRedirect

# Create your views here.

def index(request):
    if request.method =="POST":
        product = request.POST.get('product')
        print(product)
        return redirect('homepage')
    else:    
        products=Product.getallproducts()
        # print(products)
        print("session:",request.session.get('email'))
        categories = Category.get_all_categories()
        categoryID = request.GET.get('category')
        # print(categoryID)
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


def register(request):
    print(request.method)
    if request.method == "POST":
        name = request.POST.get('name')
        email=request.POST.get('email')
        password=request.POST.get('password')
        cpassword=request.POST.get('cpassword')
        phone=request.POST.get('phone')
        customer = Customer(name=name,email=email,password=password,phone=phone)
        msg= {}
        isExists = Customer.isExists(email)
        # print(email,isExists)
        if isExists:
            msg['email'] = "Email Alerady Exist"
        elif  password == cpassword:
            msg['success'] = "Registration Successfull"
            customer.save()
        else:  
             msg['pwdmatch'] ="Password does not match"  
        return render(request,"signup.html",msg)
    return render(request,"signup.html")








# def register(request):
#     if request.method =='POST':
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#         phone = request.POST.get('phone')
#         cpassword = request.POST.get('cpassword')
#         print(cpassword)
#         errormsg ={
#         } 
#         print(email)
#         isExists = Customer.isExists(email)
#         print(isExists)
#         if isExists:
#             errormsg['Emailexist'] ="Email alerady Exit"
#         else:
#             if password == cpassword:
#              customer = Customer(name =name,email=email,phone=phone,password=password)
#              customer.save()
#              errormsg['msg'] ="Registration Successfull"
             
#             else:
#                 errormsg['pwdmsg'] =" Password does not match" 

   
        
#         return render(request,"signup.html",errormsg)
#     return render(request,"signup.html")
def login(request):
    if request.method =="POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(email,password)
        customer = Customer.get_customer(email)
        
        errmsg =""
        if customer:
            
            if password== customer.password:
                request.session['email']=email
                return redirect('homepage')
            else: 
                errmsg ="Email id or password does not correct"
                return render(request,"login.html",{'errmsg':errmsg})     
                
        else:
            errmsg = "User does no exist"
            return render(request,"login.html",{'errmsg':errmsg})  
    return render(request,"login.html")

# email ="r@gmail.com"
# def isExists(self):
#         if Customer.objects.filter(email = email):
#             return HttpResponse("<h3>yes</h3>")
#         else: 
#            return False    