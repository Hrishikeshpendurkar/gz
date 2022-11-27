from unicodedata import name
from django.shortcuts import render,HttpResponse
from django.views import View

class Payment(View):
    def get(self,request):
       
        
        return render(request,'Payment.html')


    def post(self,request):
        MOP = request.POST.get('firstname')
        

        return render(request,'Payment.html')