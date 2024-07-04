from django.urls import path
from main.views import *

app_name = 'main'

urlpatterns = [
    path('', show_main, name= 'show_main'),
    path('create-barang/', create_barang, name = "create_barang"),
    path('xml/', show_xml, name = "show_xml"),
    path('json/', show_json, name = "show_json"),
    path('xml/<int:id>', show_xml_id, name = "show_xml_id"),
    path('json/<int:id>', show_json_id, name = "show_json"),
]