from unicodedata import name
from django.shortcuts import render,HttpResponse
from django.views import View
from webapp.models.user_info import User_data

class Processor(View):
    def get(self,request):
        user_d= User_data.objects.all()
        return render(request,'Processor.html',{'user_d':user_d})


    def post(self,request):
        username = request.POST.get('firstname')
        password = request.POST.get('pass')
        print(username,password)

        return render(request,'Processor.html',{'username':username})

class Processor1(View):
    def get(self,request):
        user_d= User_data.objects.all()
        return render(request,'Processor1.html',{'user_d':user_d})


    def post(self,request):
        username = request.POST.get('firstname')
        password = request.POST.get('pass')
        print(username,password)

        return render(request,'Processor1.html',{'username':username})

class Processor2(View):
    def get(self,request):
        user_d= User_data.objects.all()
        return render(request,'Processor2.html',{'user_d':user_d})


    def post(self,request):
        username = request.POST.get('firstname')
        password = request.POST.get('pass')
        print(username,password)

        return render(request,'Processor2.html',{'username':username})

class Processor3(View):
    def get(self,request):
        user_d= User_data.objects.all()
        return render(request,'Processor3.html',{'user_d':user_d})


    def post(self,request):
        username = request.POST.get('firstname')
        password = request.POST.get('pass')
        print(username,password)

        return render(request,'Processor3.html',{'username':username})
