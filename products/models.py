from django.db import models
from django.urls import reverse


class Product(models.Model):
    product_title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.PositiveIntegerField()
    category = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    # file = models.FileField(upload_to='files/')

    def get_detail_url(self):
        return reverse('products:detail', args=[self.pk])
