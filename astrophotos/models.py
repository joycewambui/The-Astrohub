from django.db import models

# Create your models here.
class Location(models.Model):
    name = models.TextField()
    
    def __str__(self):
        return self.name
    def save_location(self):
        self.save()
    
    
class Category(models.Model):
    name = models.TextField()

    def __str__(self):
        return self.name

    def save_category(self):
        self.save()
    
class Image(models.Model):
    image = models.ImageField(upload_to ='images/')
    title = models.TextField()
    location = models.ForeignKey(Location)    
    description = models.TextField()
    category = models.ForeignKey(Category)
    
    def __str__(self):
        return self.title

