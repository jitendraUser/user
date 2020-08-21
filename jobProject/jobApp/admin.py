from django.contrib import admin
from jobApp.models import jobHY,jobDel,jobNcr

# Register your models here.
class displayjobHY(admin.ModelAdmin):
    list_display=['role','skill','sal']

class displayjobDel(admin.ModelAdmin):  
    list_display=['role','skill','sal']

class displayjobNcr(admin.ModelAdmin):
    list_display=['role','skill','sal']
admin.site.register(jobHY,displayjobHY)
admin.site.register(jobDel,displayjobDel)
admin.site.register(jobNcr,displayjobNcr)
