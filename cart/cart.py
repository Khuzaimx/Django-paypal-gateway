class Cart:
    CART_KEY = 'cart'

    def __init__(self, request):
        self.session = request.session

        if self.session.session_key is None:
            self.session.create()

        cart = self.session.get(self.CART_KEY)
        if cart is None:
            cart = {}
            self.session[self.CART_KEY] = cart  # ✅ Correct syntax

        self.cart = cart

    def add(self, product):
        product_id=str(product.id)

        if product_id in self.cart:
            pass
        else:
            self.cart[product_id]  = {'price' : str(product.price)}  

        self.session.modified=True    

       
