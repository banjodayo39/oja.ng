from django.conf import settings
from django.db import models
from django.shortcuts import reverse

# Create your models here.
CATEGORY_CHOICE = (
    ('G', 'GRAINS'),
    ('V', 'VEGETABLE'),
    ('F', 'FAT_AND_OIL'),
    ('C', 'CUDIMENTS')
)

LABEL_CHOICE = (
    ('P', 'primary'),
    ('S', 'secondary'),
    ('D', 'danger')
)


class Item(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField(max_length=10)
    discount_price = models.FloatField(blank=True, null=True)
    total_price = models.FloatField(max_length=10)
    quantity = models.IntegerField(default=0)
    category = models.CharField(choices=CATEGORY_CHOICE, max_length=2)
    label = models.CharField(choices=LABEL_CHOICE, max_length=1)
    slug = models.SlugField()
    description = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self, **kwargs):
        return reverse("core:product", kwargs={
            'slug': self.slug
        })

    def get_add_to_cart_url(self):
        return reverse("core:add-to-cart", kwargs={
            'slug': self.slug
        })

    def get_remove_from_cart_url(self):
        return reverse("core:remove-from-cart", kwargs={
            'slug': self.slug
        })


class OrderItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    qty_order_item = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.qty_order_item} of {self.item.title }"


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    start_date = models.DateField(auto_now_add=True)
    order_date = models.DateField()
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
