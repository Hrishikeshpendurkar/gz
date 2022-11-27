from unicodedata import name
from django.shortcuts import render,HttpResponse
from django.views import View
from webapp.models.user_info import User_data

class Ram(View):
    def get(self,request):
        user_d= User_data.objects.all()
        return render(request,'Ram.html',{'user_d':user_d})


    def post(self,request):
        username = request.POST.get('firstname')
        password = request.POST.get('pass')
        print(username,password)

        return render(request,'Ram.html',{'username':username})

class Ram1(View):
    def get(self,request):
        user_d= User_data.objects.all()
        return render(request,'Ram1.html',{'user_d':user_d})


    def post(self,request):
        username = request.POST.get('firstname')
        password = request.POST.get('pass')
        print(username,password)

        return render(request,'Ram1.html',{'username':username})

class Ram2(View):
    def get(self,request):
        user_d= User_data.objects.all()
        return render(request,'Ram2.html',{'user_d':user_d})


    def post(self,request):
        username = request.POST.get('firstname')
        password = request.POST.get('pass')
        print(username,password)

        return render(request,'Ram2.html',{'username':username})

class Ram3(View):
    def get(self,request):
        user_d= User_data.objects.all()
        return render(request,'Ram3.html',{'user_d':user_d})


    def post(self,request):
        username = request.POST.get('firstname')
        password = request.POST.get('pass')
        print(username,password)

        return render(request,'Ram3.html',{'username':username})
