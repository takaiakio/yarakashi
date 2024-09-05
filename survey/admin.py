from django.contrib import admin
from .models import NearMiss

@admin.register(NearMiss)
class NearMissAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'encounters', 'prevention')
