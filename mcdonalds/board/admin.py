from django.contrib import admin
from .models import Category, Product, ProductOrder, Order, Staff


admin.site.register(Category)
admin.site.register(Product)
admin.site.register(ProductOrder)
admin.site.register(Order)
admin.site.register(Staff)


