from django.db import models

from products.models import Material, Operation, Quality


class Item(models.Model):
    material = models.OneToOneField(Material, null=True, on_delete=models.SET_NULL)
    quality = models.OneToOneField(Quality, null=True, on_delete=models.SET_NULL)

    class Meta:
        verbose_name = "Item"
        verbose_name_plural = "Items"

    def __str__(self):
        return f"{self.material.name} {self.quality.name}"


class Receipt(models.Model):
    items = models.ManyToManyField(Item)
    operations = models.ManyToManyField(Operation)
    transportations = models.FloatField()
    overheads = models.FloatField()
    margin = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Receipt"
        verbose_name_plural = "Receipts"

    def __str__(self):
        return f"{self.pk}"


class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    receipts = models.ManyToManyField(Receipt)

    class Meta:
        verbose_name = "Customer"
        verbose_name_plural = "Customers"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
