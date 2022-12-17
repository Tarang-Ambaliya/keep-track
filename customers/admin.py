from django.contrib import admin

from customers.models import Customer, Item, Receipt


admin.site.register(Item)
admin.site.register(Receipt)
admin.site.register(Customer)
