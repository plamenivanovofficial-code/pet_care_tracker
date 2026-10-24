from django.contrib import admin
from care_logs.models import CareActivity
# Register your models here.

@admin.register(CareActivity)
class CareActivityAdmin(admin.ModelAdmin):
    list_display = ('name', 'pet')
    