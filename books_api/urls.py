from django.urls import path
from django.urls.resolvers import URLPattern
from .views import BookList ,BookDetail

urlpatterns=[
    path('',BookList.as_view(),name='books_list' ),
    path('<int:pk>',BookDetail.as_view(),name='details')
]