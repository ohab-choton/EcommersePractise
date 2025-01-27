from django.shortcuts import render, redirect
from . models import Category, Brand, Product, ProductAttribute, Color, Size, Baner
from django.db.models import Count

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
    cats = Product.objects.values('category__title', 'category__id').distinct()
    brands = Product.objects.values('brand__title', 'brand__id').distinct()
    clr= ProductAttribute.objects.values('color__title', 'color__id', 'color__color_code').distinct()
    sizeset= ProductAttribute.objects.values('size__title', 'size__id').distinct()

    context={
        'products':products,
        'cats':cats,
        'brands':brands,
        'clr':clr,
        'sizeset':sizeset
    }
    return render(request, 'product.html',context)

def category_product_list(request, cat_id):
    category=Category.objects.get(id=cat_id)
    products=Product.objects.filter(category=category).order_by('-id')
    cats = Product.objects.values('category__title', 'category__id').distinct()
    brands = Product.objects.values('brand__title', 'brand__id').distinct()
    clr= ProductAttribute.objects.values('color__title', 'color__id', 'color__color_code').distinct()
    sizeset= ProductAttribute.objects.values('size__title', 'size__id').distinct()

    context={
        'category':category,
        'products':products,
        'cats':cats,
        'brands':brands,
        'clr':clr,
        'sizeset':sizeset
    }
    return render(request,'category_product_list.html',context)


def brand_product_list(request, brand_id):
    brand=Brand.objects.get(id=brand_id)
    products=Product.objects.filter(brand=brand).order_by('-id')
    cats = Product.objects.values('category__title', 'category__id').distinct()
    brands = Product.objects.values('brand__title', 'brand__id').distinct()
    clr= ProductAttribute.objects.values('color__title', 'color__id', 'color__color_code').distinct()
    sizeset= ProductAttribute.objects.values('size__title', 'size__id').distinct()

    context={
        'brand':brand,
        'products':products,
        'cats':cats,
        'brands':brands,
        'clr':clr,
        'sizeset':sizeset
    }
    return render(request,'brand_product_list.html',context)

def product_detail(request, slug, id):
    product = Product.objects.get(id=id)
    product_attributes = product.productattribute_set.all()
    colors=product_attributes.values('color__color_code','color__title').distinct()
    context = {
        'product': product,
        'product_attributes': product_attributes,
        'colors':colors 
    }
    return render(request, 'product_detail.html', context)

    
