from django.core.management.base import BaseCommand
from pages.models import Category

from pages.utils.helpers import read_json


class Command(BaseCommand):
    help = "Заполняет базу данных категориями из файла categories.json"

    def handle(self, *args, **options):
        categories = read_json("categories.json")
        for title in categories:
            category = Category.objects.create(title=title)
            category.save()
            print(f"Добавили категорию: {title}")


