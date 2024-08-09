from django.contrib import admin

# Register your models here.
from .models import Product, Sale

admin.site.register(Product)
admin.site.register(Sale)