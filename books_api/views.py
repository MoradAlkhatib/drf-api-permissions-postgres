from django.shortcuts import render
from rest_framework import permissions, serializers

from books_api_project.settings import REST_FRAMEWORK

# Create your views here.
from rest_framework.generics import ListCreateAPIView , RetrieveUpdateDestroyAPIView
from .models import Book
from .serializers import BookSterilizer
from .permissions import IsAuthorOrReadOnly
from rest_framework.permissions import IsAuthenticated

class BookList(ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSterilizer
    permissions_classes = (IsAuthenticated,)


class BookDetail(RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSterilizer
    permission_classes = (IsAuthorOrReadOnly,)