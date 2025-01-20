from django.db import models


# Create your models here.
class Baner(models.Model):
    baner=models.CharField(max_length=100)
    alt_img=models.CharField(max_length=100)

class Category(models.Model):
    title=models.CharField(max_length=100)
    image=models.ImageField(upload_to='categeries/' )
    def __str__(self):
        return self.title
    
class Brand(models.Model):
    title=models.CharField(max_length=100)
    image=models.ImageField(upload_to='brands/' )
    def __str__(self):
        return self.title
    
class Color(models.Model):
    title=models.CharField(max_length=100)
    color_code=models.CharField(max_length=100)
    def __str__(self):
        return self.title
class Size(models.Model):
    title=models.CharField(max_length=100)
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
    def __str__(self):
        return self.title
    
#product Attribute
class ProductAttribute(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    color=models.ForeignKey(Color,on_delete=models.CASCADE)
    size=models.ForeignKey(Size,on_delete=models.CASCADE)
    price=models.PositiveIntegerField()

    def __str__(self):
        return self.product.title
    

    
    