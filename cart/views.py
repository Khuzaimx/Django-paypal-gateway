from django.shortcuts import render, get_object_or_404
from store.models import Product
from .cart import Cart
from django.http import JsonResponse

def cart_summary(request):
    return render(request, 'cart_summary.html')

def cart_add(request):
    # Initialize the cart object
    cart = Cart(request)

    if request.method == 'POST' and request.POST.get('action') == 'post':
        # Get the product ID from the POST request
        product_id = int(request.POST.get('product_id'))

        # Ensure the product exists using get_object_or_404
        product = get_object_or_404(Product, id=product_id)

        # Add the product to the cart
        cart.add(product)

        # Return the product name in a JsonResponse
        response = JsonResponse({'product_name': product.name})
        return response

    return JsonResponse({'status': 'error', 'message': 'Invalid request method or action.'})

def cart_delete(request):
    pass

def cart_update(request):
    pass
