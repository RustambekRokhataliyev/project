from django.urls import path

from . import views

urlpatterns = [
    path("", views.index_view, name="index"),
    path("categories/", views.categories_view, name="categories"),
    path("categories/<slug:slug>/", views.products_by_category, name="category_products"),
    path("product/<slug:slug>/", views.product_detail, name="product_detail"),
    # path("favorites/", views.favorites_view, name="favorites"),
    # path("add_favorite/<slug:slug>/", views.add_to_favorite, name="add_favorite")
]
