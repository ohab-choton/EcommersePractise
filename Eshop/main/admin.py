from django.contrib import admin
from .models import Category,Brand,Color,Size,Product,ProductAttribute,Baner

# Register your models here.

admin.site.register(Size)
admin.site.register(Baner)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title','image_tag')
admin.site.register(Category,CategoryAdmin)

class BrandAdmin(admin.ModelAdmin):
    list_display = ('title','image_tag')
admin.site.register(Brand,BrandAdmin)

class ColorAdmin(admin.ModelAdmin):
    list_display = ('title','color_bg')
admin.site.register(Color,ColorAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id','title','brand', 'color', 'category','status','image_tag','is_featured')
    list_editable=('status','is_featured',)
admin.site.register(Product,ProductAdmin)


class ProductAttributeAdmin(admin.ModelAdmin):
    list_display = ('id','product','price','size','color')
admin.site.register(ProductAttribute,ProductAttributeAdmin)



