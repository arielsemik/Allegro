from django.contrib import admin
from .models import Product, ProductImages, Category

admin.site.register(ProductImages)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['cat_name_father', 'cat_name']
admin.site.register(Category, CategoryAdmin)

class ProductAdmin(admin.ModelAdmin ):
    list_display = ['product_category','name','stock', 'price']

admin.site.register(Product, ProductAdmin)



