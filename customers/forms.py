from django import forms

from customers.models import Customer, Item, Receipt


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ["material", "quality"]
        labels = {"material": "Material", "quality": "Quality"}


class ReceiptForm(forms.ModelForm):
    class Meta:
        model = Receipt
        fields = [
            "items",
            "operations",
            "transportations",
            "overheads",
            "margin",
        ]
        labels = {
            "items": "Items",
            "operations": "Operations",
            "transportations": "Transportations",
            "overheads": "Overheads",
            "margin": "Margin",
        }


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ["first_name", "last_name", "description", "receipts"]
        labels = {
            "first_name": "First Name",
            "last_name": "Last Name",
            "description": "Description",
            "receipts": "Receipts",
        }
