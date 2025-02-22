# quotes/views.py

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework import serializers  # Import serializers here
from .models import Quote
from .serializers import QuoteSerializer
from .services import QuoteService  # Import the service layer

class QuoteViewSet(viewsets.ModelViewSet):
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer

    # Specify allowed HTTP methods
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']

    def get_queryset(self):
        queryset = super().get_queryset()
        author = self.request.query_params.get('author', None)
        year_start = self.request.query_params.get('year_start', None)
        year_end = self.request.query_params.get('year_end', None)

        if author:
            queryset = queryset.filter(author__iexact=author)
        if year_start and year_end:
            queryset = queryset.filter(year__gte=year_start, year__lte=year_end)

        return queryset

    def list(self, request):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        try:
            quote = QuoteService.get_quote(pk)  # Use the service layer
            serializer = self.get_serializer(quote)
            return Response(serializer.data)
        except serializers.ValidationError as e:
            return Response(e.detail, status=status.HTTP_404_NOT_FOUND)

    def create(self, request):
        try:
            quote = QuoteService.create_quote(request.data)  # Use the service layer
            return Response(QuoteSerializer(quote).data, status=status.HTTP_201_CREATED)
        except serializers.ValidationError as e:
            return Response(e.detail, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None, partial=False):
        try:
            quote = QuoteService.update_quote(pk, request.data, partial=partial)  # Use the service layer
            return Response(QuoteSerializer(quote).data)
        except serializers.ValidationError as e:
            return Response(e.detail, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        try:
            QuoteService.delete_quote(pk)  # Use the service layer
            return Response(status=status.HTTP_204_NO_CONTENT)
        except serializers.ValidationError as e:
            return Response(e.detail, status=status.HTTP_404_NOT_FOUND)