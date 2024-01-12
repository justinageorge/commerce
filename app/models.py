from django.db import models


CATEGORY_CHOICES=(
    ('curd','curd'),
    ('milk','milk'),
    ('milkshake','milkshake'),
    ('paneer','paneer'),
    ('ghee','ghee'),
    ('cheese','cheese'),
    ('icecreams','icecreams')
)


class Product(models.Model):
    title=models.CharField(max_length=200)
    selling_price=models.FloatField()
    discounted_price=models.FloatField()
    description=models.TextField()
    composition=models.TextField(default='')
    prodapp=models.TextField(default='')
    category=models.CharField(choices=CATEGORY_CHOICES,max_length=200)
    product_image=models.ImageField(upload_to="product")

    def __str__(self):
        return self.title