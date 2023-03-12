from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

class Item(models.Model):
    user_name = models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    item_name = models.CharField(max_length=200)
    item_desc = models.CharField(max_length=200)
    item_price = models.IntegerField()
    item_image = models.CharField(max_length=500,default="https://cdn.dribbble.com/users/1012566/screenshots/4187820/media/985748436085f06bb2bd63686ff491a5.jpg?compress=1&resize=400x300&vertical=top")

    def __str__(self):
        return self.item_name   

def get_absolute_url(self):
       return reverse("foo:detail", kwargs={"pk": self.pk})