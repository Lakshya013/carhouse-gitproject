from django.contrib import admin
# Register your models here.
from django.utils.html import format_html

from .models import Team


class TeamAdmin(admin.ModelAdmin):
    def thumbnail(self,object):
        return format_html('<img src ="{}" width ="40" />'.format(object.photo.url))
    thumbnail.short_description = 'photo'

    list_display = ('id','thumbnail', 'first_name', 'last_name', 'created_date')
    list_display_links = ('id', 'first_name')
    list_filter = ['first_name', 'designation']
    search_fields = ['first_name','designation']

admin.site.register(Team,TeamAdmin)
