from django.db import models

# Create your models here.
class Detail(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=254)
    address = models.TextField(max_length=128)