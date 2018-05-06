from django.db import models

# Create your models here.
class Location(models.Model):
    place = models.TextField()

    def __str__(self):
        return self.place
class Meta:
    ordering = ['place']
    
  
    
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
    
    @classmethod
    def search_by_category(cls, search_category):
        category = cls.objects.filter(category_name_icontains=search_category)
        return category
        

