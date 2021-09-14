from django.db import models
from django.conf import settings
from django.shortcuts import reverse
from django.utils import timezone
from datetime import datetime 
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.text import slugify


# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=150, verbose_name='Title')
    slug = models.SlugField(max_length=150, unique=True,
                            allow_unicode=True, blank=True, null=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        unique_together = (('title', 'slug'),)

    def get_absolute_url(self):
        return reverse('categories', args=[self.slug])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
    
LABEL = (
    ('New','New'),
    ('Refurb','Refurb')
    )

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    discount_price = models.FloatField(blank=True, null=True)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, verbose_name='Category')
    label = models.CharField(max_length=10, choices=LABEL)
    product_details = RichTextUploadingField(blank=True, null=True)
    product_model = models.TextField(blank= True,max_length=30,  null=True)
    seller_information = models.TextField(blank= True, null=True)
    image = models.ImageField(upload_to='images',default=None, verbose_name='Thumbnail')
    product_images = models.ImageField(upload_to='images/%Y/%m/%d',blank=True, null=True)
    description = models.TextField()
    created_on = models.DateTimeField(default=datetime.now)
    slug = models.SlugField(default='test-product')
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("shop:product", kwargs={"slug": self.slug})
    def date_published(self):
        return self.created_on.strftime("%B %d, %Y %H:%M")
    
    
    
    
