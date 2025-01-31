from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Day, TextConversion
from .serializers import DaySerializer, TextConversionSerializer
from drf_yasg.utils import swagger_auto_schema
from rest_framework.parsers import MultiPartParser
from drf_yasg import openapi


class DayAPIView(APIView):
                                                                                        
    @swagger_auto_schema(
        request_body=DaySerializer,  
        responses={201: DaySerializer},
        operation_description="Create a new Day and calculate days since birth."
    )
    def post(self, request):
        serializer = DaySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TextConversionAPIView(APIView):
    parser_classes = (MultiPartParser,)
    @swagger_auto_schema(
        request_body=TextConversionSerializer,
        responses={201: TextConversionSerializer}, 
        operation_description="Convert Latin text to Cyrillic."
    )
    def post(self, request):
        serializer = TextConversionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)