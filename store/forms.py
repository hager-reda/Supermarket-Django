from django import forms
from .models import Customer, Invoice , Product, Invoice_Detail
from django.forms.formsets  import formset_factory
from django.forms  import ModelForm
from crispy_forms.helper import FormHelper

from django.forms import modelformset_factory

class customerForm(forms.ModelForm):
	class Meta:
		model = Customer
		fields = ('name','email','phone','address','block_status')

class invoiceForm(forms.ModelForm):
	class Meta:
		model = Invoice
		fields = ('shipping_address','customer','products')


class invoice_detailForm(forms.ModelForm):
	# helper = FormHelper()
	class Meta:
		model = Invoice_Detail
		fields = ('quantity',)

