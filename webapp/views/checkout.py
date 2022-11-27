from django.shortcuts import render, redirect
from django.views import View
from webapp.models.orders import Order
from webapp.models.user_info import User_data        
from webapp.models.product_info import Product  
from Gadgetzone import settings



class CheckOut(View):
    def post(self,request):
        postData = request.POST
        address = postData.get('address')
        phone = postData.get('phone')
        user_id = request.session.get('user_id')
        cart = request.session.get('cart')
        products = Product.get_products_by_id(list(cart.keys())) 

        for product in products:
            order = Order(customer = User_data(id=user_id),
                            product = product,
                            price = product.price,
                            address = address,
                            phone = phone,
                            quantity = cart.get(str(product.id)))
                            
            order.placeOrder()
        request.session['cart'] = {}
        return redirect('Orders')
