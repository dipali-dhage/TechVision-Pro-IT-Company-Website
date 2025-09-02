from django.contrib import admin
from website.models import HeroModel, BannerModel
# Register your models here.
class HeroModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'subtitle', 'button1_text', 'button2_text','image')
admin.site.register(HeroModel, HeroModelAdmin)

class BannerModelAdmin(admin.ModelAdmin):
    list_display = ('slider1_title', 'slider1_subtitle', 'slider2_title', 'slider2_subtitle', 'slider3_title', 'slider3_subtitle')
admin.site.register(BannerModel, BannerModelAdmin)