from django.db import models
from rest_framework import serializers
from .models import Book

class BookSterilizer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'title' , 'author','description','create_at','update_at')
        