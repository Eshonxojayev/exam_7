from django.shortcuts import render, redirect
from .models import Product, Category, Profile,  Rate
from .forms import RegisterForm
from django import forms
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponse


def about(request):
    return render(request, 'about.html')

def home(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    return render(request, 'index.html', {'products': products, 'categories': categories})

def contact(request):
    return render(request, 'contact.html')



def menu(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    # locations = Location.objects.all()
    rates = Rate.objects.all()
    context = {'products': products, 'categories': categories, 'rates': rates}
    return render(request, 'menu.html', context)

def service(request):
    return render(request, 'service.html')

def notpage(request):
    return render(request, '404.html')

def testimonial(request):
    return render(request, 'testimonial.html')

def team(request):
    return render(request, 'team.html')


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password1'])
            new_user.save()
            Profile.objects.create(user=new_user)
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'registration/register.html', {'form':form})

# def login(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         return render(request, 'registration/login.html', {'form':RegisterForm(), 'username':username, 'password':password})
#
#     return render(request, 'registration/login.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # 'home' URL ни киритинг
        else:
            return HttpResponse("Invalid login")
    return render(request, 'registration/login.html')