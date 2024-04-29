from django.db import models


class Admin(models.Model):
    username = models.CharField(max_length=255)
    parol = models.CharField(max_length=255)
   

    def __str__(self):
        return self.username