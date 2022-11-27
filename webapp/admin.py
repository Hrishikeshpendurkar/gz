from django.contrib import admin
from .models.user_info import User_data 
from .models.orders import Order
from .models.product_info import Product,Categories,Categories2,Categories3
from django.contrib.sessions.models import Session
# Register your models here.


class SessionAdmin(admin.ModelAdmin):           
    def _session_data(self, obj):
        return obj.get_decoded()
    list_display = ['session_key', '_session_data', 'expire_date']

class AdminUser_data(admin.ModelAdmin):
    list_display= ['id','Email']

class AdminProduct(admin.ModelAdmin):
    list_display= ['id','name','quantity']

class AdminCategories(admin.ModelAdmin):
    list_display= ['category_name', 'id']

class AdminCategories2(admin.ModelAdmin):
    list_display= ['category_name', 'id']

class AdminCategories3(admin.ModelAdmin):
    list_display= ['category_name', 'id']

class AdminOrders(admin.ModelAdmin):
    list_display= ['product', 'customer', 'quantity']

admin.site.register(User_data,AdminUser_data)
admin.site.register(Product,AdminProduct)
admin.site.register(Categories,AdminCategories)
admin.site.register(Categories2,AdminCategories2)
admin.site.register(Categories3,AdminCategories3)
admin.site.register(Session, SessionAdmin)
admin.site.register(Order, AdminOrders)