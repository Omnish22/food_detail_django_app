from django.db import models
from django.contrib.auth.models import User 
from django.urls import reverse


# Create your models here.
class Item(models.Model):
    user_name = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    item_name = models.CharField(max_length=100)
    item_description = models.CharField(max_length=200)
    item_price = models.IntegerField()
    item_image = models.CharField(max_length=600, default="https://livingstonbagel.com/wp-content/uploads/2016/11/food-placeholder.jpg")

    def __str__(self) -> str:
        return self.item_name

    # WHEN DEALING WITH CLASS BASED VIEWS WE NEED TO TELL DJANGO WHENEVER ITEM CREATED WHERE WE WANT TO REDIRECT USER 
    # CLASS BASED VIEWS CLASS HAVE NO REDIRECTION 
    def get_absolute_url(self):
        return reverse("food:detail", kwargs={"pk":self.pk})