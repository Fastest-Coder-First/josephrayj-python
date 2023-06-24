from django.contrib import admin
from .models import SearchQuery
from django.utils.html import format_html


@admin.register(SearchQuery)
class SearchQueryAdmin(admin.ModelAdmin):
    list_display = ['city_name', 'search_date','user']
    readonly_fields = ['show_weather_details']

    def show_weather_details(self, obj):
        return format_html( f'<a href="/weather/{obj.pk}/">View</a>')
    
    show_weather_details.short_description = 'Weather Details'

    

