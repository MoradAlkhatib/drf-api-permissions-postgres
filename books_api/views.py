from django.shortcuts import render
from rest_framework import serializers

from books_api_project.settings import REST_FRAMEWORK

# Create your views here.
from rest_framework.generics import ListCreateAPIView , RetrieveUpdateDestroyAPIView
from .models import Book
from .serializers import BookSterilizer

class BookList(ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSterilizer


class BookDetail(RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSterilizer