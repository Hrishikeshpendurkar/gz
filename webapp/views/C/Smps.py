from unicodedata import name
from django.shortcuts import render,HttpResponse
from django.views import View
from webapp.models.user_info import User_data

class Smps(View):
    def get(self,request):
        user_d= User_data.objects.all()
        return render(request,'Smps.html',{'user_d':user_d})


    def post(self,request):
        username = request.POST.get('firstname')
        password = request.POST.get('pass')
        print(username,password)

        return render(request,'Smps.html',{'username':username})

class Smps1(View):
    def get(self,request):
        user_d= User_data.objects.all()
        return render(request,'Smps1.html',{'user_d':user_d})


    def post(self,request):
        username = request.POST.get('firstname')
        password = request.POST.get('pass')
        print(username,password)

        return render(request,'Smps1.html',{'username':username})

class Smps2(View):
    def get(self,request):
        user_d= User_data.objects.all()
        return render(request,'Smps2.html',{'user_d':user_d})


    def post(self,request):
        username = request.POST.get('firstname')
        password = request.POST.get('pass')
        print(username,password)

        return render(request,'Smps2.html',{'username':username})

class Smps3(View):
    def get(self,request):
        user_d= User_data.objects.all()
        return render(request,'Smps3.html',{'user_d':user_d})


    def post(self,request):
        username = request.POST.get('firstname')
        password = request.POST.get('pass')
        print(username,password)

        return render(request,'Smps3.html',{'username':username})
