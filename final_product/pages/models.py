from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify
from accounts.models import CustomUser


# Create your models here.
class Category(models.Model):
    title = models.CharField(verbose_name="Название категории", max_length=255)
    slug = models.SlugField(null=True)

    def get_absolute_url(self):
        return reverse("category_products", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(verbose_name="Название продукта", max_length=255, unique=True)
    content = models.TextField(verbose_name="Описание")
    price = models.IntegerField(verbose_name="Цена")
    quantity = models.PositiveIntegerField(verbose_name="Количество", default=0)
    img_link = models.URLField(verbose_name="Ссылка на фото")
    slug = models.SlugField(null=True, unique=True)
    category = models.ForeignKey(Category, verbose_name="Категория", on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse("product_detail", kwargs={"slug": self.slug})

    def add_to_cart(self):
        return reverse("to_cart", kwargs={"product_id": self.pk, "action": "add"})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.title


# class Favorite(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="favorites")
#     product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="favorites")

class Review(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
