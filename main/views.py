from django.shortcuts import render, redirect
from main.models import Barang
from main.forms import BarangForm
from django.http import HttpResponse
from django.core import serializers

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







