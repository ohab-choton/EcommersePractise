from django.db import models

# Create your models here.
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