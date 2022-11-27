from unicodedata import name
from django.shortcuts import render,HttpResponse
from django.views import View
from webapp.models.user_info import User_data

class Laptops(View):
    def get(self,request):
        user_d= User_data.objects.all()
        return render(request,'H/Laptops.html',{'user_d':user_d})


    def post(self,request):
        username = request.POST.get('firstname')
        password = request.POST.get('pass')
        print(username,password)

        return render(request,'Laptops.html',{'username':username})

class Laptop1(View):
    def get(self,request):
        user_d= User_data.objects.all()
        return render(request,'Laptop1.html',{'user_d':user_d})


    def post(self,request):
        username = request.POST.get('firstname')
        password = request.POST.get('pass')
        print(username,password)

        return render(request,'Laptop1.html',{'username':username})

class Laptop2(View):
    def get(self,request):
        user_d= User_data.objects.all()
        return render(request,'Laptop2.html',{'user_d':user_d})


    def post(self,request):
        username = request.POST.get('firstname')
        password = request.POST.get('pass')
        print(username,password)

        return render(request,'Laptop2.html',{'username':username})

class Laptop3(View):
    def get(self,request):
        user_d= User_data.objects.all()
        return render(request,'Laptop3.html',{'user_d':user_d})


    def post(self,request):
        username = request.POST.get('firstname')
        password = request.POST.get('pass')
        print(username,password)

        return render(request,'Laptop3.html',{'username':username})
