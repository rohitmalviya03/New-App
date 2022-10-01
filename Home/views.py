from distutils.log import error
import email
import imp
from itertools import product

from threading import currentThread
from unicodedata import category, name
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.hashers import make_password,check_password
from django.conf import settings
from Home.models import Category,Product,Customer,orders
from django.views import View
from django.shortcuts import render , redirect , HttpResponseRedirect
import razorpay
from  django.views.decorators.csrf import csrf_exempt
# Create your views here.

client = razorpay.Client(
    auth=(settings.RAZOR_KEY_ID, settings.RAZOR_KEY_SECRET))

def index(request):
    # request.session['cart'].clear()
    print(settings.RAZOR_KEY_ID, settings.RAZOR_KEY_SECRET)
    if request.method == "POST":
        product = request.POST.get('product')
        delete = request.POST.get('delete')
        cart = request.session.get('cart')   
        if cart:
            qnty =cart.get(product)            
            if qnty:
                
                
                print(cart)
                if delete:
                    if qnty<=1:
                        cart.pop(product)
                    else:
                         cart[product]=qnty-1
                         print("del:",cart)                  
                else:
                    cart[product]=qnty+1
                    print("else:",cart)             
            else:
                cart[product]=1                  
        else:
            cart={}
            cart[product]=1        
        request.session['cart']=cart
        print("cart2",cart) 

        
     
        

        
        
        return redirect('homepage')
    else:    
        products=Product.getallproducts()
        # print(products)
        uname = request.session.get('customer')
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
        data['uname'] =uname
        print(data['uname'])
    
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


def login(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(email,password)
        customer = Customer.get_customer(email)
        
        msg={}
        if customer:
            if password == customer.password:
                request.session['email']=email
                request.session['customer']=customer.id
                
                msg['success'] ="Login Success"
            else:
                msg['pwdmsg'] = "Password Does not match" 
        else:
            msg['email'] = "User does not exists"           
        return redirect('homepage')
    return render(request,'login.html')
def logout(request):
    print(request.session.get('cart'))
    request.session.clear()
    print(request.session.get('cart'))
    return redirect("login")
    
def cart(request): 
    cart = request.session.get('cart')
    if cart:
        products=list(request.session.get('cart').keys())
        product =Product.get_product_by_id(products)

        print(products)
        return render(request,"cart.html",{'product':product})
    else: 
        return render(request,"cart.html",{'msg':"Empty Cart"})

def checkout(request):
    print(request.method)
    if request.method =="POST":
        address = request.POST.get('address')
        phone= request.POST.get('contact')
        amount= request.POST.get('amount')
        customer = request.session.get('customer')
        cart =request.session.get('cart')
       
        products = Product.get_product_by_id(list(cart.keys()))
        
        print(address,phone,customer,products)
        if customer:
            data = { "amount": amount, "currency": "INR", "receipt": "myorder1212" }
            order = client.order.create(data=data)
            print("dd",order)
            for product in products: 
                print("for loop")
                order = orders(customer=Customer(id=customer),price=product.price,address=address,phone=phone,product=product,quantity=cart.get(str(product.id)))
                order.save()

            request.session['cart']={} 
            print(request.session['cart'])   
        else:
            return redirect('login')    

    return render(request,'success.html') 
    
def order(request):
    customer = request.session.get('customer')
    order= orders.get_order_by_customer(customer)
    print(order)

    return render(request,'order.html',{'orders':order}) 

@csrf_exempt
def payment(request):
    CUR= "INR"
    amount =20000 
   
    # client = razorpay.Client(auth=("YOUR_ID", "YOUR_SECRET"))

    data = { "amount": 500, "currency": "INR", "receipt": "order_rcptid_11" }
    payment = client.order.create(data=data)

    # razorpay_order = razorpay_client.order.create(dict(amount=amount,currency=CUR))
    # raz_order_id = razorpay_order['id']
    # razorpay_client.order.create(razorpay_order)
    return render(request,'payment.html') 
    
    
@csrf_exempt
def success(request):
    print("payment")
    return render(request,'success.html')

    


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
# def login(request):
#     if request.method =="POST":
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#         print(email,password)
#         customer = Customer.get_customer(email)
        
#         errmsg =""
#         if customer:
            
#             if password== customer.password:
#                 request.session['email']=email
#                 return redirect('homepage')
#             else: 
#                 errmsg ="Email id or password does not correct"
#                 return render(request,"login.html",{'errmsg':errmsg})     
                
#         else:
#             errmsg = "User does no exist"
#             return render(request,"login.html",{'errmsg':errmsg})  
#     return render(request,"login.html")

# email ="r@gmail.com"
# def isExists(self):
#         if Customer.objects.filter(email = email):
#             return HttpResponse("<h3>yes</h3>")
#         else: 
#            return False    

# login POST Method


# print(request)
        # product = request.POST.get('product')
        # cart=request.session.get('cart')
        # print(cart)
        # print(product)
        # if cart:
        #     qnty =cart.get(product)
        #     if qnty:
        #         cart[product]=qnty+1
        #     else:
        #         cart[product]=1    
        # else:
        #     cart={}
        #     cart[product]=1
        # request.session['cart']=cart
        # print(cart)