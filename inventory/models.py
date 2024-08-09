from django.db import models
from datetime import date
# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    dozen_count = models.IntegerField(default=0)  # Number of dozens
    package_count = models.IntegerField(default=0)  # Number of individual packages

    def __str__(self):
        return self.name

class Sale(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity_sold = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    date = models.DateField(default=date.today)

    def save(self, *args, **kwargs):
        product = self.product
        dozens_sold = self.quantity_sold // 12
        packages_sold = self.quantity_sold % 12

        product.dozen_count -= dozens_sold
        product.package_count -= packages_sold

        if product.package_count < 0:
            product.dozen_count -= 1
            product.package_count += 12

        product.save()
        super(Sale, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.product.name} - {self.quantity_sold}"