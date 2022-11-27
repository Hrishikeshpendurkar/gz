from unicodedata import name
from django.shortcuts import render,HttpResponse
from django.views import View
from webapp.models.user_info import User_data

class Mobiles(View):
    def get(self,request):
        user_d= User_data.objects.all()
        return render(request,'Mobiles.html',{'user_d':user_d})


    def post(self,request):
        username = request.POST.get('firstname')
        password = request.POST.get('pass')
        print(username,password)

        return render(request,'Mobiles.html',{'username':username})

class Mobile1(View):
    def get(self,request):
        user_d= User_data.objects.all()
        return render(request,'Mobile1.html',{'user_d':user_d})


    def post(self,request):
        username = request.POST.get('firstname')
        password = request.POST.get('pass')
        print(username,password)

        return render(request,'Mobile1.html',{'username':username})

class Mobile2(View):
    def get(self,request):
        user_d= User_data.objects.all()
        return render(request,'Mobile2.html',{'user_d':user_d})


    def post(self,request):
        username = request.POST.get('firstname')
        password = request.POST.get('pass')
        print(username,password)

        return render(request,'Mobile2.html',{'username':username})

class Mobile3(View):
    def get(self,request):
        user_d= User_data.objects.all()
        return render(request,'Mobile3.html',{'user_d':user_d})


    def post(self,request):
        username = request.POST.get('firstname')
        password = request.POST.get('pass')
        print(username,password)

        return render(request,'Mobile3.html',{'username':username})