from django.urls import path
from . import views

urlpatterns = [
    path("",views.book_overview,name="book_overview"),
    path("<int:pk>/",views.book_detail,name="book_detail"),
    path("borrow/", views.borrow, name="borrow"),
]