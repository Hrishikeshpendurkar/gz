from django.shortcuts import render, redirect
from django.views import View
from webapp.models.orders import Order
from webapp.models.user_info import User_data        
from webapp.models.product_info import Product  
from Gadgetzone import settings
from webapp.views.Custom import Custom



class Orders(View):    
    def get(self, request):
        user_id = request.session.get('user_id')
        orders = Order.get_orders_by_customer(user_id)
        return render(request, 'orders.html', {'orders': orders})
