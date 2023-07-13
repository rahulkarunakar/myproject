from django.shortcuts import render,redirect
from django.contrib.sessions.models import Session
from django.contrib import messages
from app1.models import customer, booking
from django.http import HttpResponse
def hello (request):
      return HttpResponse("hello welcome")
def index(request):
      return render(request,'index.html')
def about(request):
      return render(request,'about.html')
def login(request):
      return render(request,"login.html")
def house(request):
      return render(request,'house.html')
def price(request):
      return render(request,'price.html')
def register(request):
      return  render(request,'register.html')
def contact(request):
      return render(request,'contact.html')

def custregdb(request):
      if request.method == "POST":
            cust = customer(uname=request.POST.get("username"),
                         password=request.POST.get("password"))
            cust.save()
      return render(request,'register.html')

def loginuser(request):
      if request.method == "POST":
            uname = request.POST.get('username')
            password = request.POST.get('password')
            try:
                  user=customer.objects.get(uname=uname, password=password)
                  request.session['user_id']=user.id
                  return render(request,"custview.html")
            except customer.DoesNotExist:
                  error_message = "Incorrect username or password"
                  messages.error(request,error_message)
      return render(request,"login.html")


# def booknow(request):
#       return render(request,'book.html')
def details(request):
      return render(request,'details.html')

def bookin(request):
      if request.method == "POST":
            book = booking(name=request.POST.get("name"),
                           phone=request.POST.get("phone"),
                           message=request.POST.get("message"),
                           variant= request.POST.get('variant'),
                           price=request.POST.get('price'))

            book.save()
      return render(request,'book.html')

def logout(request):
    Session.objects.all().delete()
    return render(request,'login.html')
