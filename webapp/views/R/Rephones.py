from unicodedata import name
from django.shortcuts import render,HttpResponse
from django.views import View
from webapp.models.user_info import User_data

class Rephones(View):
    def get(self,request):
        user_d= User_data.objects.all()
        return render(request,'Rephones.html',{'user_d':user_d})


    def post(self,request):
        username = request.POST.get('firstname')
        password = request.POST.get('pass')
        print(username,password)

        return render(request,'Rephones.html',{'username':username})

class Rephone1(View):
    def get(self,request):
        user_d= User_data.objects.all()
        return render(request,'Rephone1.html',{'user_d':user_d})


    def post(self,request):
        username = request.POST.get('firstname')
        password = request.POST.get('pass')
        print(username,password)

        return render(request,'Rephone1.html',{'username':username})

class Rephone2(View):
    def get(self,request):
        user_d= User_data.objects.all()
        return render(request,'Rephone2.html',{'user_d':user_d})


    def post(self,request):
        username = request.POST.get('firstname')
        password = request.POST.get('pass')
        print(username,password)

        return render(request,'Rephone2.html',{'username':username})

class Rephone3(View):
    def get(self,request):
        user_d= User_data.objects.all()
        return render(request,'Rephone3.html',{'user_d':user_d})


    def post(self,request):
        username = request.POST.get('firstname')
        password = request.POST.get('pass')
        print(username,password)

        return render(request,'Rephone3.html',{'username':username})