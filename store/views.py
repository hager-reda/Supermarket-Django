from django.shortcuts import render
from django.http import HttpResponse
from store.models import Customer, Product, Invoice, Invoice_Detail
from store.forms import customerForm, invoiceForm, invoice_detailForm 
from django.forms import inlineformset_factory
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, HttpResponseNotFound,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
import weasyprint
from weasyprint import HTML
from django.conf import settings
from django.template.loader import render_to_string
from django.forms.formsets import formset_factory 
from crispy_forms.helper import FormHelper

# Create your views here.

@login_required
def home(request):
    return render(request ,'./home.html')

@login_required
def allCustomers(request):
        customers = Customer.objects.filter(block_status=0).order_by('name')
        context = {'customers' : customers}
        return render(request ,'./customers.html' ,context)

@login_required
def addCustomer(request):
    new_customer = customerForm()
    if request.method=="POST":
        new_customer = customerForm(request.POST)
        if new_customer.is_valid():
            new_customer.save()
            return HttpResponseRedirect('/customers')
    return render(request,'newCustomer.html',{'new_customer': new_customer})

@login_required
def blockCustomer(request,customer_id):
    customer = Customer.objects.get(id = customer_id)
    customer.block_status = 1
    customer.save()
    return HttpResponseRedirect('/customers')


@login_required
def showCustomer(request, customer_id):
    customer= Customer.objects.get(id = customer_id)
    all_invoices = Invoice.objects.filter(customer=customer.id).order_by('created_at')
    context = {'customer' : customer, 'all_invoices' : all_invoices}
    return render(request, './showCustomer.html', context)

@login_required
def allInvoices(request):
    invoices = Invoice.objects.all().order_by('created_at')
    return render(request, './invoices.html', {'invoices':invoices})


@login_required
def showInvoice(request, invoice_id):
    details = Invoice_Detail.objects.filter(invoice = invoice_id)
    # print(details)
    total = 0
    for detail in details:
        x = Product.objects.get(id = detail.products.id)
        total += x.price 
    return render(request, './showInvoice.html', {'details' : details, 'invoice_id': invoice_id, 'total': total})


@login_required
def print(request,invoice_id):
    details = Invoice_Detail.objects.filter(invoice = invoice_id)
    invoice = Invoice.objects.get(id = invoice_id)
    total = 0
    for detail in details:
        x = Product.objects.get(id = detail.products.id)
        total += x.price
    html = render_to_string('./printInvoice.html',
                            {'details': details, 'invoice': invoice, 'total':total})
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename=\"invoice_{}.pdf"'.format(invoice_id)
    weasyprint.HTML(string=html).write_pdf(response,stylesheets=[weasyprint.CSS(settings.STATIC_ROOT + 'css/pdf.css')])
    return response

@login_required
def addInvoice(request):
    new_invoice = invoiceForm()
    helper = FormHelper()
    if request.method=="POST":
        new_invoice = invoiceForm(request.POST)
        if new_invoice.is_valid():
            products = new_invoice['products'].value()
            for product in products:
                x = Product.objects.get(id = product)
                if x.stock > 0:
                    added_invoice = new_invoice.save()
                    x.stock = x.stock - 1
                    x.save()
                    if added_invoice:
                        subject = 'Invoice'
                        messege = 'thanks for your trust. Your order is on the way '
                        from_email = settings.EMAIL_HOST_USER
                        to_email = [settings.EMAIL_HOST_USER]
                        send_mail(subject,messege,from_email, to_email, fail_silently = True)
                        invoice_detail = iinvoice_detailForm(request.POST)
                        return HttpResponseRedirect('/invoices')
                # return render(request,'invoiceProducts.html',{'invoice_detail': invoice_detail, 'products':products,'added_invoice':added_invoice,'helper':helper})
    return render(request,'newInvoice.html',{'new_invoice':new_invoice})


# @login_required
# def addInvoiceDetails(request,invoice_id):
#     formset = formset_factory(invoice_detailForm, extra=10)
#     if request.method == "POST":
#         form1 = formset(request.POST)
#         if form1.is_valid():
#             for form in form1:
#                 product_id = form.cleaned_data.get('products')
#                 product = Product.objects.get(id= product_id)
#                 quantity = form.cleaned_data.get('quantity')
#                 if product.stock > 0 :
#                     instance = Invoice_Detail.objects.create(
#                         products = product_id,
#                         invoice = invoice_id,
#                         quantity = quantity)
#                 return HttpResponseRedirect('/customers')
#     return render(request,'invoiceProducts.html',{'formset':formset})
                


#
