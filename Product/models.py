from django.db import models

class Product(models.Model):
    model = models.TextField(max_length=200)
    price = models.TextField(max_length=200)
    gbjoy = models.CharField(max_length=200)
    color = models.CharField(max_length=200)
    quantity = models.CharField(max_length=200)
    simcard = models.CharField(max_length=200)
    img = models.ImageField(upload_to = 'product/')



    def __str__(self):
        return self.model
