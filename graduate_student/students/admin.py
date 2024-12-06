from django.contrib import admin
from .models import EmploymentHistory, Graduate

class CustomEmploymentHistoryAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        if not obj.employment_placework:
            obj.employment_placework = None
        super().save_model(request, obj, form, change)

admin.site.register(EmploymentHistory, CustomEmploymentHistoryAdmin)
admin.site.register(Graduate)
