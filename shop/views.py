from django.shortcuts import render, get_object_or_404
#from cart.forms import CartAddProductForm
from .models import Category, Product
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# from django.views import generic

# class IndexView(generic.ListView):
#     template_name = 'shop/index.html'
#     context_object_name = 'products'

#     def get_queryset(self):
#         '''Return five lattest products
#         '''
#         return Product.objects.filter(created__lte=timezone.now()
#         ).order_by('-created')[:5]



def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)

    page = request.GET.get('page', 1)


    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    items_per_page = 10
    paginator = Paginator(products, items_per_page)

    try:
        # Get the products for the requested page
        products = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver the first page.
        products = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g., 9999), deliver the last page.
        products = paginator.page(paginator.num_pages)


    context = {'category': category, 'categories': categories, 'products': products}
    return render(request, 'shop/product/list.html', context)


# class ProductListView(generic.ListView):
#     template_name = 'shop/product/list.html'

#     def get_queryset(self):
#         return Product.objects.filter(available=True)

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         category = None
#         if category_slug:
#             category = get_object_or_404(Category, slug=category_slug)
#         context['category'] = category
#         context['categories'] = Category.objects.all()




from .forms import CartAddProductForm

def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm(product=product)
    context = {'product': product, 'cart_product_form': cart_product_form}
    return render(request, 'shop/product/detail.html', context)

# class ProductDetialView(generic.DetailView):

#     template_name = 'shop/product/detail.html'
#     model = Product
#     form_class = CartAddProductForm

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['products'] = get_object_or_404(Product, 
#         id=id, slug=slug, available=True)
#         return context

def product_search(request):

    query = request.GET.get("q")

    products = Product.objects.filter(name__icontains=query)

    context = {
        "products" : products,
        "query" : query,
    }


    return render(request , "shop/product/search.html" , context)