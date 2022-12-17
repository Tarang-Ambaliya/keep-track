from django.contrib import admin

from products.models import Grade, Material, Operation, Quality


admin.site.register(Quality)
admin.site.register(Grade)
admin.site.register(Operation)
admin.site.register(Material)
