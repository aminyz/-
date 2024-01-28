from django.db import models


class Food(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=100)
    price = models.CharField(null=True, max_length=20)
    image = models.ImageField(null=True, upload_to='img')

    def __str__(self):
        return self.title
