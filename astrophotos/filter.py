from django.contrib.auth.models import Image
import django_filters

class ImageFilter(django_filters.FilterSet):
    class Meta:
        model = Image
        fields = ['category','location',]