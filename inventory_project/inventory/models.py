from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Supplier(models.Model):
    name = models.CharField(max_length=150)
    contact_email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products")
    supplier = models.ForeignKey(Supplier, on_delete=models.SET_NULL, null=True, related_name="products")
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    quantity = models.PositiveIntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.name} ({self.quantity} in stock)"


class Customer(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="orders")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="orders")
    quantity = models.PositiveIntegerField()
    order_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.id} - {self.customer.name}"
