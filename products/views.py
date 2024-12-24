from django.shortcuts import render, redirect, get_object_or_404
from .models import Product

def home(request):
    return render(request, 'index.html')

def about_page(request):
    return render(request, 'about.html')

def products_list(request):
    products = Product.objects.all()
    ctx = {'products': products}
    return render(request, 'products/product-list.html', ctx)

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    ctx = {'product': product}
    return render(request, 'products/product-detail.html', ctx)

def product_create(request):
    if request.method == 'POST':
        product_title = request.POST.get('product_title')
        description = request.POST.get('description')
        price = request.POST.get('price')
        category = request.POST.get('category')
        image = request.FILES.get('image')
        if product_title and description and price and category and image:
            Product.objects.create(
                product_title=product_title,
                description=description,
                price=price,
                category=category,
                image=image
            )
            return redirect('products:list')
    return render(request, 'products/product-create.html')
