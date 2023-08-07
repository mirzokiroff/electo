from datetime import datetime
from tkinter import Image

from ckeditor.fields import RichTextField
from django.core.exceptions import ValidationError
from django.db.models import Model, CharField, ManyToManyField, DecimalField, IntegerField, TextField, ForeignKey, \
    SET_NULL, DateTimeField, PositiveSmallIntegerField, CASCADE, ImageField
from django.db.models.fields.files import ImageFieldFile


def validate_discount(value):
    if value > 100:
        raise ValidationError(
            'you cannot set more than 100% discount',
            params={"value": value}
        )


class Category(Model):
    title = CharField(max_length=255, unique=True)


class Product(Model):
    title = CharField(max_length=255)
    categories = ManyToManyField('products.Category', 'products')
    price = DecimalField(max_digits=9, decimal_places=2)
    description = RichTextField()
    colors = ManyToManyField('products.Color', 'products')
    quantity = IntegerField()
    discount = PositiveSmallIntegerField(default=0, validators=[validate_discount])
    discount_expires = DateTimeField(null=True, blank=True)

    @property
    def discounted_price(self):
        if self.discount and self.discount_expires and self.discount_expires.now() > datetime.now():
            self.discount = 0
            self.save()
            return self.price
        return self.price - (self.price // 100 * self.discount)


class Review(Model):
    text = TextField()
    user = ForeignKey('users.User', on_delete=SET_NULL, null=True)
    created_at = DateTimeField(auto_now_add=True)


class ProductImages(Model):
    product = ForeignKey('products.Product', CASCADE, 'images')
    image = ImageField(upload_to='images/products/')


class Color(Model):
    title = CharField(max_length=255)
