from django.contrib import admin
from .models import Customer,Address

class CustomerAdmin(admin.ModelAdmin):
    list_display = ['company_name', 'description']
admin.site.register(Customer,CustomerAdmin)

class AddressAdmin(admin.ModelAdmin):
    list_display = ['address_type','street','number', 'number_room', 'postal_code', 'city','tax_number']
admin.site.register(Address, AddressAdmin)
