from django.contrib import admin
from services.models import Pings

class PingsAdmin(admin.ModelAdmin):
	list_display = ('sPingAt','sSiliconID','sPacket')
	list_filter = ('sPingAt',)
	search_fields = ('sSiliconID',)

admin.site.register(Pings,PingsAdmin)
