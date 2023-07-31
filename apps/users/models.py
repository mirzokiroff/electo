from django.db.models import Model, ForeignKey, CASCADE, IntegerField, DateTimeField


class Wishlist(Model):
    product = ForeignKey('products.Product', CASCADE)
    user = ForeignKey('auth.User', CASCADE)

    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)


class Cart(Model):
    quantity = IntegerField()
    product = ForeignKey('products.Product', CASCADE)
    user = ForeignKey('auth.User', CASCADE)

    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)
