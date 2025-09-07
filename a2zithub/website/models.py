from django.db import models

# Create your models here.
# __________________________Index Page__________________________
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

class ServicesModel(models.Model):
    services_logo = models.CharField(max_length=255, null=True, blank=True)
    services_title = models.CharField(max_length=255)
    services_description = models.TextField()
    services_feature1 = models.CharField(max_length=255)
    services_feature2 = models.CharField(max_length=255)
    services_feature3 = models.CharField(max_length=255)
    services_feature4 = models.CharField(max_length=255)
    services_check_icon = models.CharField(max_length=255, null=True, blank=True)
    services_button_text = models.CharField(max_length=255)
    services_button_link = models.URLField()
    services_hidding = models.CharField(max_length=255, null=True, blank=True)
    services_sub_hidding = models.CharField(max_length=255, null=True, blank=True)
   

class TechnologyModel(models.Model):
    technology_title = models.CharField(max_length=255)
    technology_description = models.TextField()
    technology_icon = models.CharField(max_length=255, null=True, blank=True)
    technology_name = models.CharField(max_length=255)

