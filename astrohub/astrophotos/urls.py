from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns=[
    url('^$',views.home,name = 'home'),
    
    url('^planets/$', views.planets, name = 'planets'),
    url('^stars/$', views.stars, name = 'stars'),
    url('^comets/$', views.comets, name = 'comets'),
    url('^asteroids/$', views.asteroids, name = 'asteroids'),
    url('^auroras/$', views.auroras, name = 'auroras'),

]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)