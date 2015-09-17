from django.contrib import admin
from playpause.models import Log

class LogAdmin(admin.ModelAdmin):
	list_display = ('log_at','siliconid','log_value','action_taken','action_at')
	list_filter = ('log_at',)
	search_fields = ('siliconid',)

admin.site.register(Log,LogAdmin)
