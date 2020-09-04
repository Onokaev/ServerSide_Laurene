from django.contrib import admin
from .models import SocDoc

#admin.site.register(SocDoc)
@admin.register(SocDoc)
class SocDocAdmin(admin.ModelAdmin):
    list_display = ['stateOfCharge', 'depthOfCharge', 'timeStamp' ]
    list_filter = ['stateOfCharge']
    search_fields = ['timeStamp']