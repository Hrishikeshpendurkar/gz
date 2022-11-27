from django.shortcuts import render
from django.views import View
from webapp.models.user_info import User_data        
from webapp.models.product_info import Product  
from Gadgetzone import settings



class Cart(View):
    def post(self, request):
        ids = list(request.session.get('cart').keys())
        products = Product.get_products_by_id(ids)
        return render(request, 'Cart.html', {'products':products })
    def get(self, request):
        ids = list(request.session.get('cart').keys())
        products = Product.get_products_by_id(ids)
        return render(request, 'Cart.html', {'products':products })
