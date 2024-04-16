from django.contrib import admin
from .models import Task

# Register your models here.

class TaskAdmin(admin.ModelAdmin):# to show extrafileds,search_filds tags  in list page in admin task list page 
    list_display=('task','is_completed','updated_at')
    search_fields=('task',)
admin.site.register(Task,TaskAdmin)
