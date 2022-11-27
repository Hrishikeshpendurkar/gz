from django.shortcuts import render
from django.views import View
from webapp.models.user_info import User_data        
from webapp.models.product_info import Categories2  
from Gadgetzone import settings


class Custom(View):
    def get(self,request):
        firstname = request.session.get('firstname')
        user_d= User_data.objects.all()
        categories2  = Categories2.objects.all()
        CDN_DOMAIN = settings.CDN_DOMAIN

        return render(request,'Custom_Area.html',{'firstname':firstname, 
                                                'categories': categories2, 
                                                'CDN_DOMAIN':CDN_DOMAIN,})


    def post(self,request):
        username = request.POST.get('firstname')
        password = request.POST.get('pass')
        print(username,password)

        return render(request,'Custom_Area.html',{'username':username})

