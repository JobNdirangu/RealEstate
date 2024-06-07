from django.contrib import admin
from .models import Landlord

# Register your models here.
class LandlordAdmin(admin.ModelAdmin):
    list_display='land_id','name','email','contact'
admin.site.register(Landlord,LandlordAdmin)
 
