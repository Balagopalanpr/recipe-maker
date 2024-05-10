from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator,MinValueValidator

# Create your models here.

class recipe(models.Model):
    recipe_name=models.CharField(max_length=50)
    recipe_ingredients=models.CharField(max_length=50)
    instruction=models.TextField()
    cuisine=models.CharField(max_length=50)
    meal=models.CharField(max_length=50)
    created=models.DateTimeField(auto_now_add=True)
    update=models.DateTimeField(auto_now=True)


class Review(models.Model):
    recipe_name = models.ForeignKey(recipe, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.DecimalField( default=0,max_digits=2, decimal_places=1,
                                 validators=[MinValueValidator(0.0), MaxValueValidator(5.0)])
    comment = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

