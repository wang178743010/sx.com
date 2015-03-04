from django.contrib import admin
from .models import tImage,Text,company

class ImageInfoAdmin(admin.ModelAdmin):
	list_display = ("name","id",)
class TextInfoAdmin(admin.ModelAdmin):
	list_display = ("text","id")
class companyInfoAdmin(admin.ModelAdmin):
	list_display = ("name",)

admin.site.register(tImage,ImageInfoAdmin)
admin.site.register(Text,TextInfoAdmin)
admin.site.register(company,companyInfoAdmin)
