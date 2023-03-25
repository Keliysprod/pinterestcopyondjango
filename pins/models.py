from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Customer(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name=models.CharField(max_length=200, null=True)
    email=models.EmailField()

    def __str__(self):
        return self.name

class Category(models.Model):
    name=models.CharField(max_length=120)
    image=models.ImageField()
    slug = models.SlugField(max_length=120)
    

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('selected_category', kwargs={'slug': self.slug})

class Pins(models.Model):
    pic_name=models.CharField(max_length=120)
    pic_description=models.TextField()
    image=models.ImageField()
    category=models.ForeignKey(Category, on_delete=models.CASCADE)
    user=models.ForeignKey(Customer,on_delete=models.CASCADE)
    slug = models.SlugField(max_length=120, unique=True)

    def __str__(self):
        return self.pic_name
    
    def get_absolute_url(self):
        return reverse('pins_detail', kwargs={'slug': self.slug})
    

class Comments(models.Model):
    pin=models.ForeignKey(Pins, on_delete=models.CASCADE, verbose_name='изображения', blank=True, null=True, related_name='pins_comment')
    user=models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='юзер', blank=True, null=True)
    text=models.TextField(blank=True)
    created=models.DateTimeField(auto_now_add=True)


    