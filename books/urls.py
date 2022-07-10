from django.urls import path
from . import views
app_name = 'books'
urlpatterns = [
    path("",views.book_overview,name="book_overview"),
    path("<int:pk>/",views.book_detail,name="book_detail"),
    path('borrow', views.borrow, name="borrow"),
    ]
