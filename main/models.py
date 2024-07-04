from django.db import models

# Create your models here.
class Barang(models.Model):
    name = models.CharField(max_length=255)
    date_added = models.DateField(auto_now_add=True)
    amount = models.IntegerField()
    description = models.TextField(blank=True, default='')
    harga = models.IntegerField()
    


