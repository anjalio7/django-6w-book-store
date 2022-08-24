from datetime import date
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class user(AbstractUser):
    pass
class category(models.Model):
    category_name=models.CharField(max_length=50, unique=True)

class subcategory(models.Model):
    category_id=models.ForeignKey(category,on_delete=models.CASCADE,related_name='category_id')
    image = models.ImageField(upload_to = "image/")
    category_name=models.CharField(max_length=50)

    class Meta:
        unique_together = ('category_id', 'category_name',)


class book(models.Model):
    img=models.ImageField(upload_to='image/')
    subcategory_id=models.ForeignKey(subcategory,on_delete=models.CASCADE,related_name='subcategory_id')
    name=models.CharField(max_length = 1000)
    publication_year=models.CharField(max_length=50)
    publication=models.CharField(max_length=50)
    author=models.CharField(max_length=50)
    price=models.IntegerField()
    description = models.TextField(max_length=500)
    stock = models.IntegerField(default=0)


class order(models.Model):
    user_id=models.ForeignKey(user,on_delete=models.CASCADE,related_name='user_id')
    book_id=models.ForeignKey(book,on_delete=models.CASCADE,related_name='book_id')
    order_date =models.DateTimeField(auto_now_add=True)
    quantity=models.IntegerField()
    status=models.CharField(max_length=50, default = "pending")
    address=models.CharField(max_length=50)
    total_amount=models.IntegerField()


