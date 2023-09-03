from django.db import models
from django.utils.text import slugify

# Create your models here.

class Manager(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    nickname = models.CharField(max_length=30, unique=True)
    image = models.ImageField(upload_to='images/managers')
    slug = models.SlugField(blank=True, null=True)
    
    def __str__(self):
        return f'{self.name} {self.surname} : {self.nickname}'
        
    def save(self, *args, **kwargs):
        self.slug = slugify(self.nickname)
        super().save(*args, **kwargs)
        

class Product(models.Model):
    title = models.CharField(max_length=20)
    price = models.FloatField()
    description = models.TextField()
    image = models.ImageField(upload_to='images/products')
    slug = models.SlugField(blank=True, null=True)
    
    def __str__(self):
        return f'{self.title}: {self.price}'
        
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class Customer(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    nickname = models.CharField(max_length=30, unique=True)
    image = models.ImageField(upload_to='images/customers')
    slug = models.SlugField(blank=True, null=True)
        
    def __str__(self):
        return f'{self.name} {self.surname} : {self.nickname}'
        
    def save(self, *args, **kwargs):
        self.slug = slugify(self.nickname)
        super().save(*args, **kwargs)
    
    
class DeliveryCrew(models.Model):
    label = models.CharField(max_length=20, unique=True)
    image = models.ImageField(upload_to='images/delivery_crews')
    slug = models.SlugField(blank=True, null=True)
    
    def __str__(self):
        return f'{self.label}'
        
    def save(self, *args, **kwargs):
        self.slug = slugify(self.label)
        super().save(*args, **kwargs)


class Cart(models.Model):
    items = models.ManyToManyField(Product)
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE)
    total = models.FloatField(blank=True, null=True)
    