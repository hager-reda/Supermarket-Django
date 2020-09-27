from django.db import models
from datetime import datetime
from phone_field import PhoneField
# Create your models here.

class Customer(models.Model):
	name = models.CharField(max_length=200)
	email = models.EmailField(unique=True)
	phone = PhoneField(blank=True)
	address = models.TextField()
	block_status = models.BooleanField(default=False)

	def __str__(self):
		return self.name


class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField()
    stock = models.IntegerField()

    def __str__(self):
    	return self.name


class Invoice(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	customer = models.ForeignKey(Customer, on_delete=models.DO_NOTHING )
	products = models.ManyToManyField(Product, through='Invoice_Detail')
	shipping_address = models.TextField()

	def __str__(self):
		return self.shipping_address

class Invoice_Detail(models.Model):
	invoice  = models.ForeignKey(Invoice, on_delete=models.DO_NOTHING )
	products  = models.ForeignKey(Product, on_delete=models.DO_NOTHING )
	quantity = models.IntegerField(null = True)
	def __int__(self):
		return self.quantity



	# def total(self):
	# 	total = Integer()
	# 	items = self.products.all()
	# 	for ietm in items:
	# 		total = total + ietm.total()
	# 	return total
	# def __int__(self):
	# 	return self.total
    

