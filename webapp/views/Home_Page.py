from django.shortcuts import render
from django.views import View
from webapp.models.user_info import User_data        
from webapp.models.product_info import Categories        
from Gadgetzone import settings

# Create your views here.
#def home(request):
 #   return HttpResponse('This is Home Page ')

#def Home(request):
 #   return render(request,'Home_Page.html')


class Home(View):
    def get(self,request):
        cart = request.session.get('cart')
        if not cart:
            request.session['cart'] = {}
        firstname = request.session.get('firstname')
        user_d= User_data.objects.all()
        categories  = Categories.objects.all()
        CDN_DOMAIN = settings.CDN_DOMAIN

        return render(request,'Home_Page.html',{'firstname':firstname, 
                                                'categories': categories, 
                                                'CDN_DOMAIN':CDN_DOMAIN})


    def post(self,request):
        username = request.POST.get('firstname')
        password = request.POST.get('pass')
        print(username,password)

        return render(request,'Home_Page.html',{'username':username})

