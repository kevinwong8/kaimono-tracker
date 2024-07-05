from django.shortcuts import render, redirect
from main.models import Barang
from main.forms import BarangForm
from django.http import HttpResponse
from django.core import serializers
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/login')
def show_main(request):
    barangs = Barang.objects.all()
    
    context = {
        'name' : "Kevin",
        'class' : "PBP A",
        'barangs' : barangs,
        #'last_login': request.COOKIES['last_login']
    }
    return render(request, "main.html", context)

def create_barang(request):
    form = BarangForm(request.POST or None)

    if form.is_valid() and request.method== "POST":
        form.save()
        return redirect('main:show_main')
    
    context = {'form':form}
    return render(request, "create_barang.html", context)

def show_xml(request):
    data = Barang.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type = "application/xml")

def show_json_id(request, id):
    data = Barang.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data),content_type = "application/json")

def show_xml_id(request, id):
    data = Barang.objects.filter(pk = id)
    return HttpResponse(serializers.serialize("xml", data), content_type = "application/xml")

def show_json(request):
    data = Barang.objects.all()
    return HttpResponse(serializers.serialize("json", data),content_type = "application/json")

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('main:show_main')
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    return redirect('main:login')

