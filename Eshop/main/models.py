from django.db import models
from django.utils.html import mark_safe


# Create your models here.
class Baner(models.Model):
    img=models.ImageField(upload_to='baners/')
    alt_img=models.CharField(max_length=100)

    class Meta:
        verbose_name_plural='1. Baners'

    def __str__(self):
        return self.alt_img

class Category(models.Model):
    title=models.CharField(max_length=100)
    image=models.ImageField(upload_to='categeries/' )
    class Meta:
        verbose_name_plural='2. Categories'

    def image_tag(self):
        return mark_safe('<img src="%s" width="50" height="50" />' % (self.image.url))
    def __str__(self):
        return self.title
    
class Brand(models.Model):
    title=models.CharField(max_length=100)
    image=models.ImageField(upload_to='brands/' )
    class Meta:
        verbose_name_plural='3. Brands'

    def image_tag(self):
            return mark_safe('<img src="%s" width="50" height="50" />' % (self.image.url))
    def __str__(self):
        return self.title
    
class Color(models.Model):
    title=models.CharField(max_length=100)
    color_code=models.CharField(max_length=100)
    class Meta:
        verbose_name_plural='4. Colors'
    def color_bg(self):
            return mark_safe('<div style="width:50px; height:50px; background-color:%s"></div>' % (self.color_code))

    def __str__(self):
        return self.title
class Size(models.Model):
    title=models.CharField(max_length=100 ,null=True,blank=True)

    class Meta:
        verbose_name_plural='5. Sizes'
    def __str__(self):
        return self.title
    
class Product(models.Model):
    title=models.CharField(max_length=100)
    image=models.ImageField(upload_to='products/' )
    slug=models.SlugField(max_length=100)
    details=models.TextField()
    spec=models.TextField()
    brand=models.ForeignKey(Brand,on_delete=models.CASCADE)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    color=models.ForeignKey(Color,on_delete=models.CASCADE)
    size=models.ForeignKey(Size,on_delete=models.CASCADE)
    status=models.BooleanField(default=True)
    is_featured=models.BooleanField(default=False)

    class Meta:
        verbose_name_plural='6. Products'

    def image_tag(self):
            return mark_safe('<img src="%s" width="50" height="50" />' % (self.image.url))

    def __str__(self):
        return self.title
    
#product Attribute
class ProductAttribute(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    color=models.ForeignKey(Color,on_delete=models.CASCADE)
    size=models.ForeignKey(Size,on_delete=models.CASCADE, null=True, blank=True)
    price=models.PositiveIntegerField()
    class Meta:
        verbose_name_plural='7. ProductAttributes'

    def __str__(self):
        return self.product.title
    

    
    