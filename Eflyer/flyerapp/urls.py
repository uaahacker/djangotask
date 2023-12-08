from django.urls import path
from . import views


urlpatterns = [
    path("logout/",views.user_logout,name='logout'),
    path("", views.index, name="index"),
    path('base/',views.base,name='base'),
    path('cart/',views.cart,name='cart'),
    path("logout/",views.user_logout,name='logout'),
    path("delic/<int:pk>/",views.delic,name='delic'),
    

    
    
]