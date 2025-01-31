from django.contrib import admin
from .models import Day, TextConversion

@admin.register(Day)
class DayAdmin(admin.ModelAdmin):
    list_display = ('birth_date', 'days_since_birth')
    search_fields = ('birth_date',)
    list_filter = ('birth_date',)
    date_hierarchy = 'birth_date'

    @admin.display(description="Tug'ilgan kundan beri kunlar")
    def days_since_birth(self, obj):
        return obj.days_since_birth


@admin.register(TextConversion)
class TextConversionAdmin(admin.ModelAdmin):
    list_display = ('latin_text', 'cyrillic_text', 'created_at')
    search_fields = ('latin_text', 'cyrillic_text')
    list_filter = ('created_at',)
    date_hierarchy = 'created_at'

    @admin.display(description="Krill Matni")
    def cyrillic_text(self, obj):
        return obj.cyrillic_text