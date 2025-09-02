from django.db import models

# Create your models here.
class HeroModel(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.TextField()
    button1_text = models.CharField(max_length=255)
    button1_link = models.URLField()
    button2_text = models.CharField(max_length=255)
    button2_link = models.URLField()
    image = models.ImageField(upload_to='static/hero_images/')

class BannerModel(models.Model):
    slider1_title = models.CharField(max_length=255)
    slider1_subtitle = models.TextField()
    slider2_title = models.CharField(max_length=255)
    slider2_subtitle = models.TextField()
    slider3_title = models.CharField(max_length=255)
    slider3_subtitle = models.TextField()
    