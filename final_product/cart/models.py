from django.db import models

from accounts.models import CustomUser
from pages.models import Product


# Create your models here.


class Order(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_completed = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=100, null=True)
    shipping = models.BooleanField(default=False)

    @property
    def get_cart_total_quantity(self):
        order_products = self.orderproduct_set.all()
        total_quantity = sum([product.quantity for product in order_products])
        return total_quantity

    @property
    def get_cart_total_price(self):
        order_products = self.orderproduct_set.all()
        total_price = sum([product.get_total_price for product in order_products])
        return total_price


class OrderProduct(models.Model):
    """"""
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    added_at = models.DateTimeField(auto_now_add=True)

    @property
    def get_total_price(self):
        return self.product.price * self.quantity


class Customer(models.Model):
    first_name = models.CharField("Имя покупателя", max_length=255, default="")
    last_name = models.CharField("Фамилия покупателя", max_length=255, default="")
    email = models.EmailField("Почта", default="")
    phone_number = models.CharField("Номер телефона", max_length=15, default="")
    company_name = models.CharField("Название компании", max_length=255, default="")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, verbose_name="Покупатель", on_delete=models.CASCADE, null=True, blank=True,
                                 default=None)
    order = models.ForeignKey(Order, verbose_name="Заказ", on_delete=models.CASCADE, null=True, blank=True,
                              default=None)
    address_line_1 = models.TextField("Адрес 1", default="")
    address_line_2 = models.TextField("Адрес 2", default="")
    town = models.TextField("Город", default="")
    state = models.TextField("Штат", default="")

    def __str__(self):
        return f"{self.town} {self.state}"
