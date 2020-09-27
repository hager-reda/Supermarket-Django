from django.contrib import admin
from .models import Customer, Product, Invoice, Invoice_Detail
# Register your models here.


admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Invoice)
admin.site.register(Invoice_Detail)

