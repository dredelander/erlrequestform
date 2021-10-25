from django.contrib import admin
from .models import QRCode, Todos

# Register your models here.

class TodoAdmin(admin.ModelAdmin):
    readonly_fields= ('reqdate',)

admin.site.register(Todos, TodoAdmin)

admin.site.register(QRCode)
