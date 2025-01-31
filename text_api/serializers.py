from rest_framework import serializers
from .models import Day, TextConversion

class DaySerializer(serializers.ModelSerializer):
    birth_date = serializers.DateField(format="%Y-%m-%d")
    days_since_birth = serializers.ReadOnlyField()

    class Meta:
        model = Day
        fields = ['id','birth_date', 'days_since_birth']


class TextConversionSerializer(serializers.ModelSerializer):
    cyrillic_text = serializers.ReadOnlyField() 

    class Meta:
        model = TextConversion
        fields = ['id', 'latin_text', 'cyrillic_text', 'created_at']

        