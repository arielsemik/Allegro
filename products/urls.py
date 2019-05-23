from django.urls import path
from .import views


urlpatterns = [
    path('', views.index, name = 'index'),
#    path('', views.product_list, name='product_list'),
    path('<int:category_id>', views.product_list, name='product_list_by_category'),
    path('details/<int:product_id>', views.product_detail, name='product_detail'),

]
