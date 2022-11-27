from unicodedata import name
from django.shortcuts import render,HttpResponse
from django.views import View
from webapp.models.user_info import User_data

class Relaptops(View):
    def get(self,request):
        user_d= User_data.objects.all()
        return render(request,'Relaptops.html',{'user_d':user_d})


    def post(self,request):
        username = request.POST.get('firstname')
        password = request.POST.get('pass')
        print(username,password)

        return render(request,'Relaptops.html',{'username':username})

class Relaptop1(View):
    def get(self,request):
        user_d= User_data.objects.all()
        return render(request,'Relaptop1.html',{'user_d':user_d})


    def post(self,request):
        username = request.POST.get('firstname')
        password = request.POST.get('pass')
        print(username,password)

        return render(request,'Relaptop1.html',{'username':username})

class Relaptop2(View):
    def get(self,request):
        user_d= User_data.objects.all()
        return render(request,'Relaptop2.html',{'user_d':user_d})


    def post(self,request):
        username = request.POST.get('firstname')
        password = request.POST.get('pass')
        print(username,password)

        return render(request,'Relaptop2.html',{'username':username})

class Relaptop3(View):
    def get(self,request):
        user_d= User_data.objects.all()
        return render(request,'Relaptop3.html',{'user_d':user_d})


    def post(self,request):
        username = request.POST.get('firstname')
        password = request.POST.get('pass')
        print(username,password)

        return render(request,'Relaptop3.html',{'username':username})
