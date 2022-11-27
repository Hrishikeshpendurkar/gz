from unicodedata import name
from django.shortcuts import render,HttpResponse
from django.views import View
from webapp.models.user_info import User_data

class Cabinet(View):
    def get(self,request):
        user_d= User_data.objects.all()
        return render(request,'Cabinet.html',{'user_d':user_d})


    def post(self,request):
        username = request.POST.get('firstname')
        password = request.POST.get('pass')
        print(username,password)

        return render(request,'Cabinet.html',{'username':username})

class Cabinet1(View):
    def get(self,request):
        user_d= User_data.objects.all()
        return render(request,'Cabinet1.html',{'user_d':user_d})


    def post(self,request):
        username = request.POST.get('firstname')
        password = request.POST.get('pass')
        print(username,password)

        return render(request,'Cabinet1.html',{'username':username})

class Cabinet2(View):
    def get(self,request):
        user_d= User_data.objects.all()
        return render(request,'Cabinet2.html',{'user_d':user_d})


    def post(self,request):
        username = request.POST.get('firstname')
        password = request.POST.get('pass')
        print(username,password)

        return render(request,'Cabinet2.html',{'username':username})

class Cabinet3(View):
    def get(self,request):
        user_d= User_data.objects.all()
        return render(request,'Cabinet3.html',{'user_d':user_d})


    def post(self,request):
        username = request.POST.get('firstname')
        password = request.POST.get('pass')
        print(username,password)

        return render(request,'Cabinet3.html',{'username':username})
