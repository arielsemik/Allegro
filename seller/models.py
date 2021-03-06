from django.db import models
from multiselectfield import MultiSelectField

class Seller(models.Model):
    company_name = models.CharField(max_length=200,verbose_name='Nazwa firmy')
    description = models.CharField(max_length=1000, verbose_name='Opis firmy')
    def __str__(self):
        return self.company_name



class Address(models.Model):
    address_types = ((1,'Fakturowania'), (2,'Dostawy'), (3,'Siedziba'))
    company = models.ForeignKey(Seller, on_delete=models.CASCADE, default=None)
    address_type = MultiSelectField(choices=address_types, max_length=3, max_choices=3)
    street = models.CharField(max_length=100)
    number = models.PositiveSmallIntegerField(blank=True)
    number_room = models.CharField(max_length=10, blank=True)
    postal_code = models.PositiveSmallIntegerField(blank=True, null=True)
    city = models.CharField(max_length=40)
    tax_number = models.IntegerField(unique=True)
