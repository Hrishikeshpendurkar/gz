from unicodedata import name
from django.shortcuts import render,HttpResponse
from django.views import View
from webapp.models.user_info import User_data

class Storage(View):
    def get(self,request):
        user_d= User_data.objects.all()
        return render(request,'Storage.html',{'user_d':user_d})


    def post(self,request):
        username = request.POST.get('firstname')
        password = request.POST.get('pass')
        print(username,password)

        return render(request,'Storage.html',{'username':username})

class Storage1(View):
    def get(self,request):
        user_d= User_data.objects.all()
        return render(request,'Storage1.html',{'user_d':user_d})


    def post(self,request):
        username = request.POST.get('firstname')
        password = request.POST.get('pass')
        print(username,password)

        return render(request,'Storage1.html',{'username':username})

class Storage2(View):
    def get(self,request):
        user_d= User_data.objects.all()
        return render(request,'Storage2.html',{'user_d':user_d})


    def post(self,request):
        username = request.POST.get('firstname')
        password = request.POST.get('pass')
        print(username,password)

        return render(request,'Storage2.html',{'username':username})

class Storage3(View):
    def get(self,request):
        user_d= User_data.objects.all()
        return render(request,'3.html',{'user_d':user_d})


    def post(self,request):
        username = request.POST.get('firstname')
        password = request.POST.get('pass')
        print(username,password)

        return render(request,'Storage3.html',{'username':username})
