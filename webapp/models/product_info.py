from turtle import Screen
from django.db import models
from datetime import datetime


class Categories(models.Model):
    category_name = models.CharField(max_length=25,default=None, null=False, blank=False)
    product_image = models.ImageField(
        upload_to='static/images/uploads/product_image/', blank=True,
        default = None , null =True
    )
    def __str__(self) -> str:
         return self.category_name

class Categories2(models.Model):
    category_name = models.CharField(max_length=25,default=None, null=False, blank=False)
    product_image = models.ImageField(
        upload_to='static/images/uploads/product_image/', blank=True,
        default = None , null =True
    )
    def __str__(self) -> str:
         return self.category_name

class Categories3(models.Model):
    category_name = models.CharField(max_length=25,default=None, null=False, blank=False)
    product_image = models.ImageField(
        upload_to='static/images/uploads/product_image/', blank=True,
        default = None , null =True
    )
    def __str__(self) -> str:
         return self.category_name


class Product(models.Model):
    name= models.CharField(max_length=100,default=None, null=False, blank=False)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, default=None, null=True, blank=True )
    category2 = models.ForeignKey(Categories2, on_delete=models.CASCADE, default=None, null=True, blank=True )
    category3 = models.ForeignKey(Categories3, on_delete=models.CASCADE, default=None, null=True, blank=True )
    price = models.CharField(max_length=10,default=0, null=False, blank=False)
    product_image = models.ImageField(
        upload_to='static/images/uploads/product_image/', blank=True,
        default = None , null =True
    )
    short_desc = models.CharField(max_length=50,default=None, null=True, blank=True)
    quantity = models.CharField(max_length=25,default=None, null=True, blank=True)
    full_desc = models.CharField(max_length=255,default=None, null=True, blank=True)
    date_listed = models.DateTimeField( default=datetime.now())
    is_available = models.BooleanField(default=True)
    #features
    Model_Name= models.CharField(max_length=100,default=None, null=True, blank=True)
    Brand= models.CharField(max_length=100,default=None, null=True, blank=True)
    Processor= models.CharField(max_length=100,default=None, null=True, blank=True)
    GPU = models.CharField(max_length=100,default=None, null=True, blank=True)
    Ram= models.CharField(max_length=100,default=None, null=True, blank=True)
    Storage= models.CharField(max_length=100,default=None, null=True, blank=True)
    Operating_System= models.CharField(max_length=100,default=None, null=True, blank=True)
    Colour= models.CharField(max_length=100,default=None, null=True, blank=True)
    Connector_Type= models.CharField(max_length=100,default=None, null=True, blank=True)
    Special_Feature= models.CharField(max_length=100,default=None, null=True, blank=True)
    Cuda_Cores= models.CharField(max_length=100,default=None, null=True, blank=True)
    Memory_Size= models.CharField(max_length=100,default=None, null=True, blank=True)
    Interface_Width= models.CharField(max_length=100,default=None, null=True, blank=True)
    Display_Connectors= models.CharField(max_length=100,default=None, null=True, blank=True)
    Socket= models.CharField(max_length=100,default=None, null=True, blank=True)
    Chipset= models.CharField(max_length=100,default=None, null=True, blank=True)
    Dimensions= models.CharField(max_length=100,default=None, null=True, blank=True)
    Form_Factor= models.CharField(max_length=100,default=None, null=True, blank=True)
    Platform= models.CharField(max_length=100,default=None, null=True, blank=True)
    Core= models.CharField(max_length=100,default=None, null=True, blank=True)
    Series= models.CharField(max_length=100,default=None, null=True, blank=True)
    Threads= models.CharField(max_length=100,default=None, null=True, blank=True)
    Unlocked= models.CharField(max_length=100,default=None, null=True, blank=True)
    Memory_Slot= models.CharField(max_length=100,default=None, null=True, blank=True)
    Size= models.CharField(max_length=100,default=None, null=True, blank=True)
    Boast_Clock= models.CharField(max_length=100,default=None, null=True, blank=True)
    Maximum_Resolution= models.CharField(max_length=100,default=None, null=True, blank=True)
    Kit_Type= models.CharField(max_length=100,default=None, null=True, blank=True)
    Certification= models.CharField(max_length=100,default=None, null=True, blank=True)
    Modular= models.CharField(max_length=100,default=None, null=True, blank=True)
    Wattage= models.CharField(max_length=100,default=None, null=True, blank=True)
    Capacity= models.CharField(max_length=100,default=None, null=True, blank=True)
    Screen= models.CharField(max_length=100,default=None, null=True, blank=True)


    @staticmethod
    def get_products_by_id(ids):
        return Product.objects.filter(id__in = ids)

    def __str__(self) -> str:
         return self.name

    def isExists(Product_Name):
            if Product.objects.filter(Product_Name=Product_Name):
                return True
            return False