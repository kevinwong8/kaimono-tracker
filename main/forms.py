from django.forms import ModelForm
from main.models import Barang

class BarangForm(ModelForm):
    class Meta:
        model = Barang
        fields = ["name", "amount", "description", "harga"]