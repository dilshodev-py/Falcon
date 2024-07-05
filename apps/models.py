from django.db import models
from django.db.models import Model, CharField, TextField, DecimalField, ForeignKey, ImageField, FloatField, \
    IntegerField, SlugField
from django.utils.text import slugify


class BaseModel(Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = SlugField(unique=True)

    class Meta:
        abstract = True

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug = slugify(self.name)
        while self.__class__.objects.filter(slug=self.slug).exists():
            self.slug += '-1'
        super().save(force_insert, force_update, using, update_fields)

class Category(BaseModel):
    class Meta:
        verbose_name_plural = 'Categories'

    name = CharField(max_length=50)

    def __str__(self):
        return self.name


class Product(BaseModel):
    name = CharField(max_length=255)
    description = TextField()
    price = FloatField()
    category = ForeignKey('apps.Category', on_delete=models.CASCADE, related_name='products')
    shipping_price = FloatField()
    quantity = IntegerField()
    discount = IntegerField()

    def __str__(self):
        return self.name


class Specification(Model):
    key = CharField(max_length=50)
    value = CharField(max_length=255)
    product = ForeignKey('apps.Product', on_delete=models.CASCADE, related_name='specifications')

    def __str__(self):
        return self.key


class ProductImage(Model):
    image = ImageField(upload_to='products/')
    product = ForeignKey('apps.Product', on_delete=models.CASCADE, related_name='images')

    def __str__(self):
        return self.image
