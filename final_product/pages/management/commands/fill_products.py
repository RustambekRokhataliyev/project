from django.core.management.base import BaseCommand
from pages.models import Category, Product

from pages.utils.helpers import read_json
import random
from django.utils.text import slugify


class Command(BaseCommand):
    help = "заполняем базу продуктами"

    def __get_category_obj(self, category_name: str):
        category = Category.objects.get(title=category_name)
        return category

    def handle(self, *args, **options):
        data = read_json("products.json")

        for item in data:
            category = self.__get_category_obj(item["category_name"])

            for product in item["products"]:
                price = product["product_current_price"].replace("сум", "").replace(" ", "")
                try:
                    price = int(price) // 11258.29
                    product_obj = Product.objects.create(
                        title=product["product_name"],
                        content=product["description"],
                        price=price,
                        quantity=random.choice(list(range(1, 50))),
                        img_link=product["product_img_url"],
                        slug=slugify(product["product_name"]),
                        category=category
                    )
                    product_obj.save()
                    print(f"Добавлен продукт: {product['product_name']}")
                except Exception as e:
                    print(e)