from django.conf.urls.static import static
from django.urls import path
from app1 import views
from home import settings

urlpatterns=[
    path('index/',views.index),
    path('about/',views.about),
    path('login/', views.login),
    path('house/', views.house),
    path('price/',views.price),
    path('register/',views.register),
    path('contact/',views.contact),
    path('custreg/',views.custregdb),
    path('custview/',views.loginuser),
    path('details/',views.details),
    path('booked/',views.bookin),
    path('logout/', views.logout),


]