from atexit import register
from django import template

register = template.Library()
@register.filter(name="is_in_cart")
def is_in_cart(product,cart):
    keys = cart.keys()
    print(keys)     #{{product|is_in_cart:request.session.cart}}
    for id in keys:
        if int(id) == product.id:
            return True
    print(product)
    return False



@register.filter(name="cart_qunty")
def cart_qunty(product,cart):
    keys = cart.keys()
    for id in keys:
        if int(id) == product.id:
            return cart.get(id)
    print(product)
    return 0

@register.filter(name="total_price")
def total_price(product,cart):
    keys = cart.keys()
    for id in keys:
        if int(id) == product.id:
            return product.price*cart_qunty(product,cart)
    print(product)
    return 0

@register.filter(name="total_cart_price")
def total_cart_price(product,cart):
    keys = cart.keys()
    print(keys)
    sum=0
    for p in product:
        sum=sum+total_price(p,cart)
    return sum    
     
@register.filter(name="price_in_rupees")
def price_in_rupees(product,cart):
    keys = cart.keys()
    print(keys)
    sum=0
    for p in product:
        sum=sum+total_price(p,cart)*100
    return sum         