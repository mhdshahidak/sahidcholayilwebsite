from django.urls import path
from .import views

app_name = 'web'

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('updates', views.updates, name='updates'),
    path('gallery', views.gallery, name='gallery'),
    path('position', views.position, name='position'),
    path('awards', views.awards, name='awards'),
    path('contact', views.contact, name='contact'),
]
