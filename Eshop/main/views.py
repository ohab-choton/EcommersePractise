from django.shortcuts import render, redirect
from . models import Category, Brand, Product, ProductAttribute, Color, Size, Baner
from django.db.models import Count, Max, Min
from django.http import JsonResponse
from django.template.loader import render_to_string

from . import views

# Create your views here.
def home(request):
    banners=Baner.objects.all().order_by('-id') 
     
    data=Product.objects.filter(is_featured=True).order_by('-id')
    
    context={'banners':banners,'data':data}
    return render(request, 'index.html',context)

def category_list(request):
    cattegories=Category.objects.all().order_by('-id')
    context={
        'cattegories':cattegories
    }
    return render(request, 'categories.html',context)
def brand_list(request):
     #brands that have products with valid product attribute images.
     brands = Brand.objects.filter(product__productattribute__image__isnull=False).distinct()
     context={
        'brands':brands
    }
     return render(request, 'brand.html',context)

def product_list(request):
    products=Product.objects.all().order_by('-id')
    #pass to to context processor
    max_price=ProductAttribute.objects.aggregate(Max('price'))
    min_price=ProductAttribute.objects.aggregate(Min('price'))

    context={
        'products':products,
        'max_price':max_price,
        'min_price':min_price
    }
    return render(request, 'product.html',context)

def category_product_list(request, cat_id):
    category=Category.objects.get(id=cat_id)
    products=Product.objects.filter(category=category).order_by('-id')
    #pass to to context processor
    context={'products':products}
    return render(request,'category_product_list.html',context)


def brand_product_list(request, brand_id):
    brand=Brand.objects.get(id=brand_id)
    products=Product.objects.filter(brand=brand).order_by('-id')
    #pass to to context processor
    context={'products':products}
    return render(request,'brand_product_list.html',context)

def product_detail(request, slug, id):
    product = Product.objects.get(id=id)
    product_attributes = product.productattribute_set.all()
    colors=product_attributes.values('color__color_code','color__title').distinct()
    
    related_products = Product.objects.filter(category=product.category).exclude(id=id)[:4]
    context = {
        'product': product,
        'product_attributes': product_attributes,
        'colors':colors,
        'related_products': related_products 
    }
    return render(request, 'product_detail.html', context)

def search(request):
    #q is the name of the input field in the search form in the base.html
    q=request.GET['q'] 
    data=Product.objects.filter(title__icontains=q).order_by('-id')
    
    context={'data':data}
    return render(request, 'search.html',context)


def filter_data(request):
    colors = request.GET.getlist('color[]') # 'color[] if came from filter.html , similar rest of category , brand size
    categories = request.GET.getlist('category[]')
    brands = request.GET.getlist('brand[]')
    sizes = request.GET.getlist('size[]')

    allproducts = Product.objects.all()

    # Apply filters if selected
    if len(colors)>0:
        allproducts = allproducts.filter(productattribute__color__id__in=colors).distinct()
    if categories:
        allproducts = allproducts.filter(category__id__in=categories).distinct()
    if brands:
        allproducts = allproducts.filter(brand__id__in=brands).distinct()
    if sizes:
        allproducts = allproducts.filter(productattribute__size__id__in=sizes).distinct()

    t = render_to_string('ajax/product-list.html', {'products': allproducts})

    return JsonResponse({'data': t})

    
