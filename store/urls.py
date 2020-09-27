"""supermarket URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from django.conf.urls import url, include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns



urlpatterns = [
    # path('home', views.home),
    url(r'^home/$', views.home, name = 'home'),
    url(r'^customers/$', views.allCustomers),
    url(r'^invoices/$', views.allInvoices),
    url(r'^customers/(?P<customer_id>[\w]+)$', views.showCustomer),
    url(r'^invoices/(?P<invoice_id>[\w]+)$', views.showInvoice),
    url(r'^newCustomer/$', views.addCustomer),
    url(r'^newInvoice/$', views.addInvoice),
    url(r'^block/(?P<customer_id>[\w]+)$', views.blockCustomer),
    # url(r'^newInvoice/invoiceDetail/(?P<invoice_id>[\w]+)$', views.addInvoiceDetails),
    url(r'^print/(?P<invoice_id>[\w]+)$', views.print),




]

urlpatterns += staticfiles_urlpatterns()

