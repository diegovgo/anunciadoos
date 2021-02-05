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
    url = models.CharField(max_length=64, blank=True)
    phone = models.IntegerField(null=True, blank=True)
    published = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Store(models.Model):
    name = models.CharField(max_length=120)
    description = models.CharField(max_length=120)
    published = models.BooleanField(default=False)
    category = models.ManyToManyField(Category, related_name="store")
    district = models.ManyToManyField(District, related_name="store")
    logo = models.ImageField(upload_to="static/logos", null=True)
    url = models.CharField(max_length=64, blank=True)
    phone = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name

class Storesubcategory(models.Model):
    name = models.CharField(max_length=64)
    store = models.ForeignKey(Store, null=True, on_delete=models.CASCADE, related_name="storesubcategory")
    title = models.CharField(max_length=64,blank=True)
    order = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.title

class Article(models.Model):
    name = models.CharField(max_length=120)
    published = models.BooleanField(default=False)
    description = models.TextField()
    img = models.ImageField(upload_to="static/imgs", null=True, blank=True, default="static/imgs/article_default.jpg")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    storesubcategory = models.ForeignKey(Storesubcategory, null=True, on_delete=models.CASCADE, related_name="article")
   
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

class TypeOf(models.Model):
    name = models.CharField(max_length=64)
    restaurante = models.ForeignKey(Restaurant, null=True, on_delete=models.CASCADE, related_name="typeof")
    title = models.CharField(max_length=64,blank=True)
    order = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.title
class Dishes(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField()
    img = models.ImageField(upload_to="static/imgs", null=True, blank=True, default="static/imgs/food_default.jpg")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    typeof = models.ForeignKey(TypeOf, null=True, on_delete=models.CASCADE, related_name="dishes")
    published = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class TypesOfFood(models.Model):
    name = models.CharField(max_length=64)
    restaurant = models.ManyToManyField(Dishes, related_name="typeoffood")

    def __str__(self):
        return self.name