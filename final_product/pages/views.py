from django.core.paginator import Paginator
from django.shortcuts import render, redirect

from .forms import ReviewForm
from .models import Category, Product, Review


# Create your views here.
def index_view(request):
    products = Product.objects.all()[:8]
    context = {
        "products": products
    }
    return render(request, "pages/index.html", context)


def categories_view(request):
    if request.method == "POST":

        if "sort" in request.POST:
            query = request.POST.get("sort")
            products = Product.objects.all().order_by(query)
        else:
            min_cost = request.POST.get("min_cost").replace("$", "")
            max_cost = request.POST.get("max_cost").replace("$", "")
            products = Product.objects.filter(price__range=[int(min_cost), int(max_cost)])
    else:
        products = Product.objects.all()

    count = products.count()

    paginator = Paginator(products, 6)
    page_number = request.GET.get("page")
    paged_products = paginator.get_page(page_number)

    context = {
        "products": paged_products,
        "count": count
    }
    return render(request, "pages/categories.html", context)


def products_by_category(request, slug):
    category = Category.objects.get(slug=slug)

    if request.method == "POST":
        if "sort" in request.POST:
            query = request.POST.get("sort")
            products = Product.objects.filter(category=category).order_by(query)
        else:
            min_cost = request.POST.get("min_cost").replace("$", "")
            max_cost = request.POST.get("max_cost").replace("$", "")
            products = Product.objects.filter(category=category, price__range=[int(min_cost), int(max_cost)])
    else:
        products = Product.objects.filter(category=category)

    count = products.count()

    paginator = Paginator(products, 6)
    page_number = request.GET.get("page")
    paged_products = paginator.get_page(page_number)

    context = {
        "products": paged_products,
        "count": count
        # "category": category
    }
    return render(request, "pages/categories.html", context)


def product_detail(request, slug):

    product = Product.objects.get(slug=slug)

    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.product = product
            form.save()
            return redirect("product_detail", slug)
    else:
        form = ReviewForm()

    reviews = Review.objects.filter(
        product=product
    )

    related_products = Product.objects.filter(category=product.category)
    related_products = list(filter(lambda x: x != product, related_products))

    context = {
        "product_detail": product,
        "related_products": related_products[:4],
        "form": form,
        "reviews": reviews
    }
    return render(request, "pages/product_detail.html", context)

# def add_to_favorite(request, slug):
#     user = auth.get_user(request)
#     if user.is_authenticated:
#         product = Product.objects.get(slug=slug)
#         product.favorites.add(product)
#         return redirect("favorites")
#
#
# def favorites_view(request):
#     products = Product.objects.all()
#     context = {
#         "products": products
#     }
#     return render(request, "pages/favorites.html", context)
