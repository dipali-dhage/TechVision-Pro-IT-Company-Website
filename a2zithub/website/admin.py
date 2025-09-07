from django.contrib import admin
from website.models import HeroModel, BannerModel, ServicesModel, TechnologyModel
# Register your models here.
class HeroModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'subtitle', 'button1_text', 'button2_text','image')

class BannerModelAdmin(admin.ModelAdmin):
    list_display = ('slider1_title', 'slider1_subtitle', 'slider2_title', 'slider2_subtitle', 'slider3_title', 'slider3_subtitle')

class ServicesModelAdmin(admin.ModelAdmin):
    list_display = ('services_title', 'services_description', 'services_feature1', 'services_feature2', 'services_feature3', 'services_feature4', 'services_check_icon', 'services_button_text', 'services_button_link')

class TechnologyModelAdmin(admin.ModelAdmin):
    list_display = ('technology_title', 'technology_description', 'technology_icon', 'technology_name')

admin.site.register(HeroModel, HeroModelAdmin)
admin.site.register(BannerModel, BannerModelAdmin)
admin.site.register(ServicesModel, ServicesModelAdmin)
admin.site.register(TechnologyModel, TechnologyModelAdmin)
