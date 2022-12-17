from django.urls import path

from customers import views


urlpatterns = [
    path("item/", views.item_form, name="item form"),
    path("receipt/", views.receipt_form, name="receipt form"),
    path("customer/", views.customer_form, name="customer form"),
    path("list/", views.list_customers, name="list customers"),
]
