from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.loginUser, name="login"),
    path("logout", views.logoutUser, name="logout"),
    path("buy/<int:book_id>", views.buy, name="buy"),
    path("delete/<int:book_id>", views.delete, name="delete"),
]
