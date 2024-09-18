from django.shortcuts import render,redirect
import requests
from django.contrib.auth.decorators import login_required
from .models import Product
# Create your views here.


def index(request):
    try:
        if request.session['token']:
            respons = requests.get('https://fakestoreapi.com/products')
            products = respons.json()
            return render(request, 'index.html', {'products': products})
    except Exception as e:
        print('Error⚠️⚠️⚠️⚠️: %s' % e)
        return redirect('login')

def add_product(request):
    respons = requests.get('https://fakestoreapi.com/products')
    products = respons.json()
    for p in products:
        Product.objects.create(title=p['title'], price=p['price'], description=p['description'], image=p['image'])
    return redirect('index')


def login_page(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        response = requests.post('https://fakestoreapi.com/auth/login', json={
            'username': username,
            'password': password
        })
        if response.status_code == 200:
            print('login successful: ' + response.json()['token'])
            print('__________________###################')
            request.session['token'] = response.json()['token']
            return redirect('index')
        else:
            context = {'error': 'Invalid credentials'}
            print('Error: %s' % response.status_code)
            return render(request, 'login.html', context)
    return render(request, 'login.html')

def logout_view(request):
    request.session.flush()
    return redirect('login')