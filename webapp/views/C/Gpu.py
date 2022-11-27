from unicodedata import name
from django.shortcuts import render,HttpResponse
from django.views import View
from webapp.models.user_info import User_data

class Gpu(View):
    def get(self,request):
        user_d= User_data.objects.all()
        return render(request,'Gpu.html',{'user_d':user_d})


    def post(self,request):
        username = request.POST.get('firstname')
        password = request.POST.get('pass')
        print(username,password)

        return render(request,'Gpu.html',{'username':username})

class Gpu1(View):
    def get(self,request):
        user_d= User_data.objects.all()
        return render(request,'Gpu1.html',{'user_d':user_d})


    def post(self,request):
        username = request.POST.get('firstname')
        password = request.POST.get('pass')
        print(username,password)

        return render(request,'Gpu1.html',{'username':username})

class Gpu2(View):
    def get(self,request):
        user_d= User_data.objects.all()
        return render(request,'Gpu2.html',{'user_d':user_d})


    def post(self,request):
        username = request.POST.get('firstname')
        password = request.POST.get('pass')
        print(username,password)

        return render(request,'Gpu2.html',{'username':username})

class Gpu3(View):
    def get(self,request):
        user_d= User_data.objects.all()
        return render(request,'Gpu3.html',{'user_d':user_d})


    def post(self,request):
        username = request.POST.get('firstname')
        password = request.POST.get('pass')
        print(username,password)

        return render(request,'Gpu3.html',{'username':username})
