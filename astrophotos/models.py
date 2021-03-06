from django.db import models


# Create your models here.
class Location(models.Model):
    name = models.TextField()
    


    def __str__(self):
        return self.name

    
    class Meta:
        ordering = ['name']
    
    
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
        return self.category
    
    @classmethod
    def my_images(cls):
        images = cls.objects.all()
        return images
    
    def delete_images(self):
        self.remove()
    
    def save_images(self):
        self.save()
    
    def search_image(category):
        pass

    def filter_by_location(location):
        pass

    def update_image(self, id):
        pass

    def get_image_by_id(id):
        pass
    

   
        

