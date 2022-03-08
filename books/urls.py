
from django.urls import path, include
from . import views as books_views
urlpatterns = [
    path('', books_views.list_books, name="list_books")
]