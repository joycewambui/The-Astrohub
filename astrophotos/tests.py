from django.test import TestCase
from .models import Location,Image

# Create your tests here.


# Create your tests here.

class GalleryTestClass(TestCase):
    def setUp(self):
        self.photos=Image(image='image',title='name',description='describe')
#Testign instance
    def test_instance(self):
        self.assertTrue(isinstance(self.images,Image))

#Testing save Method
def test_save_method(self):
    self.photos.save_images()
    gallery = Image.objects.all()
    self.assertTrue(len( image)> 0)
