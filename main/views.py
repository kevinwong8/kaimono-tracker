from django.shortcuts import render, redirect
from main.models import Barang

# Create your views here.
def show_main(request):
    barangs = Barang.objects.all()
    
    context = {
        'name' : "Kevin",
        'class' : "PBP A",
        'barangs' : barangs,
        #'last_login': request.COOKIES['last_login']
    }
    return render(request, "main.html", context)