from django.contrib.auth.models import User

from core import settings
from pages.models import Product
from .models import Order, OrderProduct
from accounts.models import CustomUser


class CartForAuthenticatedUser:
    def __init__(self, request, product_id=None, action=None):
        self.user = request.user

        if product_id and action:
            if action == "delete_product":
                self.delete_product_from_cart(product_id)
            else:
                self.add_or_delete(product_id, action)

    def get_cart_info(self):
        user, created = CustomUser.objects.get_or_create(
            # user=self.user,
            username=self.user.username,
            email=self.user.email
        )

        order, created = Order.objects.get_or_create(
            user=user
        )
        order_products = order.orderproduct_set.all()
        cart_total_quantity = order.get_cart_total_quantity
        cart_total_price = order.get_cart_total_price

        return {
            "cart_total_quantity": cart_total_quantity,
            "cart_total_price": cart_total_price,
            "order": order,
            "products": order_products
        }

    def add_or_delete(self, product_id, action):
        order = self.get_cart_info()["order"]

        product = Product.objects.get(pk=product_id)

        order_product, created = OrderProduct.objects.get_or_create(
            order=order,
            product=product
        )

        if action == "add" and product.quantity > 0:  # если товара больше 0
            order_product.quantity += 1  # увеличиваем кол-во в заказе
            product.quantity -= 1  # уменьшаем кол-во на складе
        else:
            order_product.quantity -= 1
            product.quantity += 1

        product.save()
        order_product.save()

        if order_product.quantity <= 0:
            order_product.delete()

    def clear(self):
        order = self.get_cart_info()["order"]

        order_products = order.orderproduct_set.all()
        for product in order_products:
            product.delete()

        order.save()

    def delete_product_from_cart(self, product_id):
        order = self.get_cart_info()["order"]

        order_product = order.orderproduct_set.get(product=product_id)
        order_product.delete()


class CartFormAnonymousUser:
    def __init__(self, request, product_id=None, action=None):
        self.session = request.session
        self.cart = self.get_cart()

        if product_id and action:
            self.key = str(product_id)
            self.product = Product.objects.get(pk=product_id)
            self.cart_product = self.cart.get(self.key)

            if action == "add" and self.product.quantity > 0:
                self.add()
            elif action == "delete":
                self.delete()

            self.product.save()
            self.save()

    def get_cart(self):
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session["cart"] = {}
        return cart

    def save(self):
        self.session.modified = True  # обновляем сессию

    def get_cart_info(self):
        products = []
        order = {
            "get_cart_total_price": 0,
            "get_cart_total_quantity": 0,
            "shipping": True
        }
        cart_total_quantity = order["get_cart_total_quantity"]
        cart_total_price = order["get_cart_total_price"]
        for key in self.cart:
            if self.cart[key]["quantity"] > 0:
                product_quantity = self.cart[key]["quantity"]
                cart_total_quantity += product_quantity
                product = Product.objects.get(pk=key)
                get_total_price = product.price * product_quantity

                cart_product = {
                    "pk": product.pk,
                    "product": {
                        "pk": product.pk,
                        "title": product.title,
                        "price": product.price,
                        "img_link": product.img_link,
                        "quantity": product.quantity,
                        "get_absolute_url": product.get_absolute_url()
                    },
                    "quantity": product_quantity,
                    "get_total_price": get_total_price
                }

                products.append(cart_product)
                order["get_cart_total_price"] += cart_product["get_total_price"]
                order["get_cart_total_quantity"] += cart_product["quantity"]
                cart_total_price = order["get_cart_total_price"]

        self.save()

        return {
            "cart_total_quantity": cart_total_quantity,
            "cart_total_price": cart_total_price,
            "order": order,
            "products": products
        }

    def add(self):
        if self.cart_product:
            self.cart_product["quantity"] += 1
        else:
            self.cart[self.key] = {
                "quantity": 1
            }
        self.product.quantity -= 1

    def delete(self):
        self.cart_product["quantity"] -= 1
        self.product.quantity += 1

        if self.cart_product["quantity"] <= 0:
            del self.cart[self.key]

    def clear(self):
        self.cart.clear()


def get_cart_data(request):
    if request.user.is_authenticated:
        user_cart = CartForAuthenticatedUser(request)
        cart_info = user_cart.get_cart_info()
    else:
        session_cart = CartFormAnonymousUser(request)
        cart_info = session_cart.get_cart_info()

    return {
        "cart_total_quantity": cart_info["cart_total_quantity"],
        "cart_total_price": cart_info["cart_total_price"],
        "order": cart_info["order"],
        "products": cart_info["products"]
    }


# def anonymous_order(request, data):
#     name = data["name"]
#     email = data["email"]
#
#     cart = CartFormAnonymousUser(request)
#     cart_info = cart.get_cart_info()
#
#     user, created = User.objects.get_or_create(
#         name=name,
#         email=email
#     )
#
#     items = cart_info["products"]
#
#     order = Order.objects.create(user=user)
#
#     for item in items:
#         product = Product.objects.get(pk=item["pk"])
#         OrderProduct.objects.create(
#             product=product,
#             order=order,
#             quantity=item["quantity"]
#         )
#
#     return user, order
