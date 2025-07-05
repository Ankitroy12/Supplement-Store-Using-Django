from django.shortcuts import render
from django.shortcuts import HttpResponse
from core.models import Contact
from django.contrib import messages
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login, logout
from .middlewares import auth

def home(request):
   return render(request,'index.html')

def about(request):
   return render(request,'about.html')

def protein(request):
   return render(request,'protein.html')

def creatine(request):
   return render(request,'creatine.html')

def supplements(request):
   return render(request,'supplements.html')
                 
def medicine(request):
   return render(request,'medicine.html')

def contact(request):
   sup = request.GET.get('sup')
   if request.method == "POST":
      name = request.POST.get('name')
      number = request.POST.get('number')
      address = request.POST.get('address')
      sup = request.POST.get('sup')
      contact= Contact(name=name,number=number,address=address,sup=sup)
      contact.save()
      messages.success(request, "Thank you for choosing LifeLine! Your supplement has been booked successfully! We’ll deliver it within 20 minutes.")
      
   return render(request,'contact.html',{'sup': sup})


def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('dashboard')
    else:
        initial_data = {'username':'', 'password1':'', 'password2':''}
        form = UserCreationForm(initial=initial_data)
    return render(request,'register.html',{'form':form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            return redirect('dashboard')
    else:
        initial_data = {'username':'', 'password':''}
        form = AuthenticationForm(initial=initial_data)
    return render(request,'login.html',{'form':form})

@auth
def dashboard_view(request):
    return render(request,'index.html')

def logout_view(request):
    logout(request)
    return redirect('login')
