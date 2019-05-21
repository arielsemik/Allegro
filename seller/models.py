from django.db import models

class Seller(models.Model):
    company_name = models.CharField(max_length=200,verbose_name='Nazwa firmy')
    description = models.CharField(max_length=1000, verbose_name='Opis firmy')


class Address(models.Model):
    address_types = ('Fakturowania', ' Dostawy', 'Siedziba')

    address_type = models.CharField(max_length=100, choices=address_types)
    street = models.CharField(max_length=100)
    number = models.PositiveSmallIntegerField(blank=True)
    number_room = models.CharField(max_length=10, blank=True)
    postal_code = models.PositiveSmallIntegerField(blank=True)
    city = models.CharField(max_length=40)
    tax_number = models.IntegerField(unique=True)
