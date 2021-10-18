from django.contrib import admin
from .models import StockOut

# Register your models here.

class StockOutAdmin(admin.ModelAdmin):
    readonly_fields= ('date',)

admin.site.register(StockOut, StockOutAdmin)