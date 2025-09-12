from django.contrib import admin
from website.models import HeroModel, BannerModel, ServicesModel, TechnologyModel, IndustriesModel, WhyChooseUsModel, CaseStudyModel, TestimonialsModel, PartnerModel, CTAModel
# Register your models here.
class HeroModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'subtitle', 'button1_text', 'button2_text','image')

class BannerModelAdmin(admin.ModelAdmin):
    list_display = ('slider1_title', 'slider1_subtitle', 'slider2_title', 'slider2_subtitle', 'slider3_title', 'slider3_subtitle')

class ServicesModelAdmin(admin.ModelAdmin):
    list_display = ('services_title', 'services_description', 'services_feature1', 'services_feature2', 'services_feature3', 'services_feature4', 'services_check_icon', 'services_button_text', 'services_button_link')

class TechnologyModelAdmin(admin.ModelAdmin):
    list_display = ( 'technology_icon', 'technology_name')

class IndustriesModelAdmin(admin.ModelAdmin):
    list_display = ('industries_icon', 'industries_name')

class WhyChooseUsModelAdmin(admin.ModelAdmin):
    list_display = ('choose_icon', 'choose_name', 'choose_description')

class CaseStudyModelAdmin(admin.ModelAdmin):
    list_display = ('case_title', 'case_tag', 'case_image', 'case_button_text', 'case_button_link')

class TestimonialsModelAdmin(admin.ModelAdmin):
    list_display = ('client_content', 'author_name', 'author_position', 'author_image')

class PartnerModelAdmin(admin.ModelAdmin):
    list_display = ()

class CTAModelAdmin(admin.ModelAdmin):
    list_display = ('cta_button_text', 'cta_button_url')

admin.site.register(HeroModel, HeroModelAdmin)
admin.site.register(BannerModel, BannerModelAdmin)
admin.site.register(ServicesModel, ServicesModelAdmin)
admin.site.register(TechnologyModel, TechnologyModelAdmin)
admin.site.register(IndustriesModel, IndustriesModelAdmin)
admin.site.register(WhyChooseUsModel, WhyChooseUsModelAdmin)    
admin.site.register(CaseStudyModel, CaseStudyModelAdmin)
admin.site.register(TestimonialsModel, TestimonialsModelAdmin)
admin.site.register(PartnerModel, PartnerModelAdmin)    
admin.site.register(CTAModel, CTAModelAdmin)

# ____________About Page______________________________ About Page ______________________About Page_____________________

