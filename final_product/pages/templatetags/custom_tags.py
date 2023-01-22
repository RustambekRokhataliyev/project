from django.template import Library

from cart.utils import get_cart_data
from pages.models import Category

register = Library()


@register.simple_tag()
def get_categories():
    categories = Category.objects.all()
    return categories


@register.simple_tag(name="products_on_page")
def count_products_on_page(page, on_page, products_count):
    if page == 1:
        return on_page
    return (products_count - on_page) + on_page


@register.simple_tag(name="cart_quantity")
def get_cart_quantity(request):
    cart_info = get_cart_data(request)
    return cart_info["cart_total_quantity"]


# @register.simple_tag(name="count_products")
# def count_products(category_slug=None):
#     path = list(filter(lambda x: x != "", category_slug.split("/")))
#     if len(path) > 1:
#         category = Category.objects.get(slug=path[-1])
#         products = Product.objects.filter(category=category)
#         return products.count()
#     return Product.objects.all().count()
