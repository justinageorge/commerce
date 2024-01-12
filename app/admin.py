from django.contrib import admin
from app.models import Product

@admin.register(Product)
class productModelAdmin(admin.ModelAdmin):
    list_display=["id","title","discounted_price","category","product_image"]

