from django.http import HttpResponse
from django.shortcuts import render

from customers.forms import CustomerForm, ItemForm, ReceiptForm
from customers.models import Customer


def item_form(request):
    if request.method == "POST":
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ItemForm()
    return render(request, "customers.html", {"form": form, "heading": "Item"})


def receipt_form(request):
    if request.method == "POST":
        form = ReceiptForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ReceiptForm()
    return render(request, "customers.html", {"form": form, "heading": "Receipt"})


def customer_form(request):
    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = CustomerForm()
    return render(request, "customers.html", {"form": form, "heading": "Customer"})


def list_customers(request):
    if request.method == "GET":
        return HttpResponse(Customer.objects.all())
