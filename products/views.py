from django.shortcuts import render

from django.shortcuts import render
from .models import Product, Category


def index_view(request):
    products = Product.objects.all().order_by('-created_at')
    categories = Category.objects.all()

    context = {
        'products': products,
        'categories': categories,
    }
    return render(request, 'index.html', context)


from django.contrib.auth.decorators import login_required

from django.shortcuts import render, redirect
from .models import Product


def my_products_view(request):
    if not request.user.is_authenticated:
        return redirect('login')

    my_products = Product.objects.filter(seller=request.user).order_by('-created_at')

    query = request.GET.get('q')
    if query:
        my_products = my_products.filter(title__icontains=query)

    context = {
        'my_products': my_products,
        'search_query': query,
    }

    return render(request, 'my_products.html', context)


from django.shortcuts import render, get_object_or_404
from .models import Product


def product_detail_view(request, pk):
    product = get_object_or_404(Product, pk=pk)

    related_products = Product.objects.filter(category=product.category).exclude(pk=pk)[:4]

    context = {
        'product': product,
        'related_products': related_products,
    }
    return render(request, 'product_detail.html', context)


from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Product



def product_edit_view(request, pk):
    product = get_object_or_404(Product, pk=pk, seller=request.user)

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, "Mahsulot muvaffaqiyatli yangilandi!")
            return redirect('my_products')
    else:
        form = ProductForm(instance=product)

    return render(request, 'product_form.html', {'form': form, 'product': product})


def product_delete_view(request, pk):
    product = get_object_or_404(Product, pk=pk, seller=request.user)

    if request.method == 'POST':
        product.delete()
        messages.warning(request, "Mahsulot o'chirildi.")
        return redirect('my_products')

    return redirect('my_products')
