from django.urls import path, include
from .views.Home_Page import Home
from .views.Product import ShowProducts,ShowProducts2,ShowProducts3,ProductDetails
from .views.Cart import Cart
from .views.checkout import CheckOut
from .views.orders import Orders
from .views.Login_signup import Login,Register, logout
from .views.Custom import Custom
from .views.Refurbhished import Refurbhished
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',Home.as_view(),name="Home_page"),
    path('Ct/',Custom.as_view(),name="Ct"),
    path('Login/',Login.as_view(),name="Login"),
    path('logout/',logout,name="logout"),
    path('Register/',Register.as_view(),name="Register"),
    path('cart/', Cart.as_view(), name='cart'),
    path('check-out/', CheckOut.as_view(), name='CheckOut'),
    path('orders/', Orders.as_view(), name='Orders'),
    path('Rb/',Refurbhished.as_view(),name="Rb"),
    path('products/<id>', ShowProducts.as_view(), name='show_product'),
    path('products2/<id>', ShowProducts2.as_view(), name='show_product2'),
    path('products3/<id>', ShowProducts3.as_view(), name='show_product3'),
    path('product_details/<id>', ProductDetails.as_view(), name='product_details'),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
