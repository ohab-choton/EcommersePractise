from . models import  Product, ProductAttribute
def get_filters(request):
    cats = Product.objects.values('category__title', 'category__id').distinct()
    brands = Product.objects.values('brand__title', 'brand__id').distinct()
    clr= ProductAttribute.objects.values('color__title', 'color__id', 'color__color_code').distinct()
    sizeset= ProductAttribute.objects.values('size__title', 'size__id').distinct()
    context={
        'cats':cats,
        'brands':brands,
        'clr':clr,
        'sizeset':sizeset,
    }
    return context


