from django.db import models


class Status(models.Model):
    name = models.CharField(max_length=100)


class Type(models.Model):
    name = models.CharField(max_length=100)


class Category(models.Model):
    name = models.CharField(max_length=100)
    type = models.ForeignKey(
        Type,
        related_name="categories",
        on_delete=models.CASCADE)


class Subcategory(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(
        Category,
        related_name="subcategories",
        on_delete=models.CASCADE)


class Transaction(models.Model):
    created_at = models.DateField(auto_now_add=True)
    status = models.ForeignKey(
        Status,
        related_name="transactions",
        on_delete=models.PROTECT)
    type = models.ForeignKey(
        Type,
        related_name="transactions",
        on_delete=models.PROTECT)
    category = models.ForeignKey(
        Category,
        related_name="transactions",
        on_delete=models.PROTECT)
    subcategory = models.ForeignKey(
        Subcategory,
        related_name="transactions",
        on_delete=models.PROTECT)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    comment = models.TextField(blank=True)
