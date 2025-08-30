from .cart import Cart

def cart_context(request):
    my_cart = Cart(request)   # ✅ assign to a variable
    return {'cart': my_cart}  # ✅ return in dictionary
