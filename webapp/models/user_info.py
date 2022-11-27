from django.db import models
from datetime import datetime

class User_data(models.Model):
    firstname= models.CharField(max_length=25,default=None, null=False, blank=False)
    lastname = models.CharField(max_length=25,default=None, null=True, blank=True)
    date_joined = models.DateTimeField( default=datetime.now())
    Email = models.EmailField(max_length=100, null=False, blank=False, unique=True)
    Mobile_No = models.CharField(max_length=12, null=True, blank=True)
    Address = models.CharField(max_length=25,default=None, null=True, blank=True)
    password = models.CharField(max_length=254, default=None,  null=False, blank=False)
    is_active = models.BooleanField(default=True)

    def __str__(self) -> str:
         return self.Email

    def isExists(email):
            if User_data.objects.filter(Email=email):
                return True
            return False






#    
#     GENDER_CHOICE = (
#         ('Female', 'Female'),
#         ('Male', 'Male'),
#         ('Other', 'Other')
#     )
#     USER_TYPE = (
#         ('Freemium', 'Freemium'),
#         ('Premium ', 'Premium'),
#         ('Professional ', 'Professional')
#     )
#     email_address = models.EmailField(max_length=100, null=False, blank=False, unique=True)
#     is_active = models.BooleanField(default=True)
#     gender = models.CharField(choices=GENDER_CHOICE, max_length=10, default=None, blank=True, null=True)
#     user_type = models.CharField(choices=USER_TYPE, max_length=15, default='Freemium', null=True)
#     password = models.CharField(max_length=254, default=None,  null=False, blank=Fal
#     password = models.CharField(max_length=254, default=None,  null=False, blank=False)
#     profile_image = models.ImageField(
#         upload_to='uploads/profile_images/', blank=True,
#         default = 'uploads/profile_images/dummy_boy3.jpg' , null =True
#     )
#     date_joined = models.DateTimeField( default=datetime.now())
#     terms_and_conditions = models.BooleanField( default=True)

#     def __str__(self):
#         return self.email_address
    
#     def register(self):
#         self.save()

#     @staticmethod
#     def get_user_by_email(email):
#         try:
#             return RegisterdUser.objects.get(email_address=email)
#         except:
#             return False
# def is_exists(email):
#         if RegisterdUser.objects.filter(email_address=email):
#             return True
#         return False