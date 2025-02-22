# quotes/services.py

from .models import Quote
from .serializers import QuoteSerializer
from rest_framework import serializers

class QuoteService:
    @staticmethod
    def create_quote(data):
        serializer = QuoteSerializer(data=data)
        if serializer.is_valid():
            return serializer.save()
        else:
            raise serializers.ValidationError(serializer.errors)

    @staticmethod
    def update_quote(quote_id, data, partial=False):
        try:
            quote = Quote.objects.get(id=quote_id)
        except Quote.DoesNotExist:
            raise serializers.ValidationError("Quote not found.")

        serializer = QuoteSerializer(quote, data=data, partial=partial)
        if serializer.is_valid():
            return serializer.save()
        else:
            raise serializers.ValidationError(serializer.errors)

    @staticmethod
    def get_quote(quote_id):
        try:
            return Quote.objects.get(id=quote_id)
        except Quote.DoesNotExist:
            raise serializers.ValidationError("Quote not found.")

    @staticmethod
    def delete_quote(quote_id):
        try:
            quote = Quote.objects.get(id=quote_id)
            quote.delete()
            return True
        except Quote.DoesNotExist:
            raise serializers.ValidationError("Quote not found.")