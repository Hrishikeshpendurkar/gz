from unicodedata import name
from django.shortcuts import render,HttpResponse
from django.views import View
from webapp.models.user_info import User_data

class Mb(View):
    def get(self,request):
        user_d= User_data.objects.all()
        return render(request,'Mb.html',{'user_d':user_d})


    def post(self,request):
        username = request.POST.get('firstname')
        password = request.POST.get('pass')
        print(username,password)

        return render(request,'Mb.html',{'username':username})

class Mb1(View):
    def get(self,request):
        user_d= User_data.objects.all()
        return render(request,'Mb1.html',{'user_d':user_d})


    def post(self,request):
        username = request.POST.get('firstname')
        password = request.POST.get('pass')
        print(username,password)

        return render(request,'Mb1.html',{'username':username})

class Mb2(View):
    def get(self,request):
        user_d= User_data.objects.all()
        return render(request,'Mb2.html',{'user_d':user_d})


    def post(self,request):
        username = request.POST.get('firstname')
        password = request.POST.get('pass')
        print(username,password)

        return render(request,'Mb2.html',{'username':username})

class Mb3(View):
    def get(self,request):
        user_d= User_data.objects.all()
        return render(request,'Mb3.html',{'user_d':user_d})


    def post(self,request):
        username = request.POST.get('firstname')
        password = request.POST.get('pass')
        print(username,password)

        return render(request,'Mb3.html',{'username':username})
