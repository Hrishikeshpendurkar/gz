from turtle import pos
from django.shortcuts import render,redirect
from django.views import View
from webapp.models.product_info import Product
from Gadgetzone import settings

class ShowProducts(View):
    def post(self,request):
        postData = request.POST
        product_id = postData.get('product_id')
        product_data = Product.objects.get(id=product_id)
        CDN_DOMAIN = settings.CDN_DOMAIN
        if id:
            product_data = Product.objects.filter(category__id = id)
        
        return render(request, 'product_details.html',{'product_data': product_data, 'CDN_DOMAIN':CDN_DOMAIN} )
    def get(self,request, id=None):
        product_data = Product.objects.all()
        if id:
            product_data = Product.objects.filter(category__id = id)
        
        CDN_DOMAIN = settings.CDN_DOMAIN
        
        return render(request, 'show_products.html',{'product_data': product_data, 'CDN_DOMAIN':CDN_DOMAIN})


class ShowProducts2(View):
    def post(self,request):
        postData = request.POST
        product_id = postData.get('product_id')
        product_data = Product.objects.get(id=product_id)
        CDN_DOMAIN = settings.CDN_DOMAIN
        if id:
            product_data = Product.objects.filter(category2__id = id)
        
        return render(request, 'product_details.html',{'product_data': product_data, 'CDN_DOMAIN':CDN_DOMAIN} )
    def get(self,request, id=None):
        product_data = Product.objects.all()
        if id:
            product_data = Product.objects.filter(category2__id = id)
        
        CDN_DOMAIN = settings.CDN_DOMAIN
        
        return render(request, 'show_products2.html',{'product_data': product_data, 'CDN_DOMAIN':CDN_DOMAIN})


class ShowProducts3(View):
    def post(self,request):
        postData = request.POST
        product_id = postData.get('product_id')
        product_data = Product.objects.get(id=product_id)
        CDN_DOMAIN = settings.CDN_DOMAIN
        if id:
            product_data = Product.objects.filter(category3__id = id)
        
        return render(request, 'product_details.html',{'product_data': product_data, 'CDN_DOMAIN':CDN_DOMAIN} )
    def get(self,request, id=None):
        product_data = Product.objects.all()
        if id:
            product_data = Product.objects.filter(category3__id = id)
        
        CDN_DOMAIN = settings.CDN_DOMAIN
        
        return render(request, 'show_products3.html',{'product_data': product_data, 'CDN_DOMAIN':CDN_DOMAIN})


class ProductDetails(View):

    def post(self,request, id=None):
        postData = request.POST
        product_id = postData.get('product_id')
        remove = postData.get('remove')
        cart = request.session.get('cart')
        stock = None
        try:
            product_data = Product.objects.get(id=product_id)
            stock = product_data.quantity
        except:
            pass
        if cart:
            quantity = cart.get(product_id)
            if quantity:
                if remove:
                    if quantity<=1:
                        cart.pop(product_id)
                    else:
                        cart[product_id] = quantity-1
                else:
                    # user can't select more than stock
                    if not int(stock) == int(quantity):
                        cart[product_id] = quantity+1      
            else:
                cart[product_id] = 1
        else:
            cart = {}
            cart[product_id] = 1
        
        request.session['cart'] = cart

        CDN_DOMAIN = settings.CDN_DOMAIN
        product_data = Product.objects.filter(id = id).first()

        return render(request, 'product_details.html',{'product_data': product_data, 'CDN_DOMAIN':CDN_DOMAIN} )

    def get(self,request, id=None):
        CDN_DOMAIN = settings.CDN_DOMAIN
        product_data = Product.objects.filter(id = id).first()

        return render(request, 'product_details.html',{'product_data': product_data, 'CDN_DOMAIN':CDN_DOMAIN} )
    

# def cart(request):
#     cart = request.session.get('cart')
#     keys = cart.keys()
#     pd_list = []
#     for id in keys:
#         if int(id):
#             pd_list.append(Product.objects.filter(id=id).first())
#     print(pd_list)
#     return render( request, 'cartt.html',{'pd_list':pd_list})
