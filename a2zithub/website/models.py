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
    technology_icon = models.CharField(max_length=255,blank=True)
    technology_name = models.CharField(max_length=255)

class IndustriesModel(models.Model):
    industries_icon = models.CharField(max_length=255, null=True, blank=True)
    industries_name = models.CharField(max_length=255)

class WhyChooseUsModel(models.Model):
    choose_icon = models.CharField(max_length=255, null=True, blank=True)
    choose_name = models.CharField(max_length=255)
    choose_description = models.TextField()

class CaseStudyModel(models.Model):
    case_title = models.CharField(max_length=255)
    case_tag = models.CharField(max_length=255)
    case_image = models.ImageField(upload_to='static/case_study_images/')
    case_problem_icon = models.CharField(max_length=255, null=True, blank=True)
    case_problem_text = models.TextField()
    case_solution_icon = models.CharField(max_length=255, null=True, blank=True)
    case_solution_text = models.TextField()
    case_result_icon = models.CharField(max_length=255, null=True, blank=True)
    case_result_text = models.TextField()
    case_technologies = models.CharField(max_length=255)
    case_button_text = models.CharField(max_length=255)
    case_button_link = models.URLField()

class TestimonialsModel(models.Model):
    client_content = models.TextField()
    author_name = models.CharField(max_length=255)
    author_position = models.CharField(max_length=255)
    author_image = models.ImageField(upload_to='static/testimonial_images/')

class PartnerModel(models.Model):
   partner_logo = models.ImageField(upload_to='static/partner_logos/')

class CTAModel(models.Model):
    cta_button_text = models.CharField(max_length=255)
    cta_button_url = models.URLField() 


# ______About Page____________________ About Page_____________________About Page_________________About Page_____
