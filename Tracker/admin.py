from django.contrib import admin
from .models import States
# Register your models here.

class StateData(admin.ModelAdmin):
    list_display = ['id','State']

admin.site.register(States,StateData)