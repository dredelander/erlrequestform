from django.contrib import admin
from .models import Todos

# Register your models here.

class TodoAdmin(admin.ModelAdmin):
    readonly_fields= ('reqdate',)

admin.site.register(Todos, TodoAdmin)


