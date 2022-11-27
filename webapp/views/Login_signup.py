from unicodedata import name
from django.shortcuts import render,HttpResponse,redirect
from django.views import View
from webapp.models.user_info import User_data
from django.contrib.auth.hashers import make_password,check_password

class Register(View):

    def post(self,request):
        try:
            postData = request.POST
            firstname = postData.get('firstname')
            lastname = postData.get('lastname')
            Email = postData.get('Email')
            Mobile_No = postData.get('Mobile_No')
            Address = postData.get('Address')
            password1 = postData.get('password')
            password2 = postData.get('password2')

            error_message = None

            register_user = User_data(firstname=firstname,
                                    lastname= lastname,
                                    Address = Address,
                                    Mobile_No= Mobile_No, 
                                    Email=Email,
                                    password=password1
            )
            print(postData,"==========================")
            valid_data, error_message = validate_user(postData)
            if not valid_data:
                return render(request, 'Register.html', {'error_message': error_message})

            password_hash = make_password(password1)
            register_user.password = password_hash
            register_user.save()
            registered_user = User_data.objects.filter(Email=Email).first()
            request.session['user_id'] = registered_user.id
            request.session['firstname'] = registered_user.firstname
            return redirect('Login')

        except Exception as e:
            print(e)
            return render(request, 'Register.html', {'error_message': e})


    def get(self, request):
        return render(request, 'Register.html')

def validate_user(postData):
    error_message = None
    try:
        firstname = postData.get('firstname')
        Email = postData.get('Email') 
        password1 = postData.get('password') 
        password2 = postData.get('password2')

        if firstname == None or type(firstname)!= type('string')or len(firstname)<4:
            return False, 'Plese Enter First Name Correctly minimun 4 charactors'
        if Email == None or type(Email)!= type('string') or User_data.isExists(Email):
            return False, 'Email Is Wrong Or Alrady Exists '

        if password1 == None or len(password1)<8:
            return False, 'Plese Enter Password Correctly minimun 8 charectors'
        if password1 != password2:
            return False, 'Password Does not Match'

    except Exception as e:
        return False, e
    return True, ''


class Login(View):
    def get(self,request):
        Email = ''
        
        return render(request,'Login.html',{'Email':Email})


    def post(self,request):
        postData = request.POST
        Email = postData.get('Email')
        password1 = postData.get('password')
        user_exists = User_data.isExists(Email)
        error_message = 'Wrong Email or Password'

        if not user_exists:
            return render(request, 'login.html', {'error_message': error_message})

        registered_user = User_data.objects.filter(Email=Email).first()
        user_password = registered_user.password

        if not check_password(password1, user_password):
            return render(request, 'Login.html', {'error_message': error_message})

        request.session['user_id'] = registered_user.id
        request.session['firstname'] = registered_user.firstname
        return redirect('Home_page')
    

def logout(request):
    request.session.clear()
    return redirect('Login')