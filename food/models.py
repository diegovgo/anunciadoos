from django.db import models

# Create your models here.
class District(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name


class Restaurant(models.Model):
    name = models.CharField(max_length=120)
    category = models.ManyToManyField(Category, related_name="restaurant")
    district = models.ManyToManyField(District, related_name="restaurant")
    logo = models.ImageField(upload_to="static/logos", null=True)

    def __str__(self):
        return self.name

class Saludinst(models.Model):
    name = models.CharField(max_length=120)
    category = models.ManyToManyField(Category, related_name="saludinst")
    district = models.ManyToManyField(District, related_name="saludinst")
    logo = models.ImageField(upload_to="static/logos", null=True)
    description = models.TextField()
    url= models.CharField(max_length=120, blank=True)

    def __str__(self):
        return self.name

class Dishes(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField()
    img = models.ImageField(upload_to="static/imgs", null=True, blank=True, default="static/imgs/food_default.jpg")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    restaurant = models.ForeignKey(Restaurant, null=True, on_delete=models.CASCADE, related_name="dishes")

    def __str__(self):
        return self.name

