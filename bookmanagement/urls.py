from django.urls import path
from . import views

urlpatterns = [
    path('', views.BookRetrieve.as_view(), name="book"),
    # path('', views.BookList.as_view(), name="book"),
    # path('',views.List.as_view(), name='book'),
    path('create/', views.BookCreate.as_view(), name="book_create"),
    path('<int:id>', views.BookDetail.as_view(), name="BookDetail"),
    path('<int:pk>/update/', views.BookUpdateView.as_view(), name="BookUpdate"),
    path('<int:pk>/delete/', views.BookDelete.as_view(), name="BookDelete"),
    path('detail/<int:book_id>', views.BookSystemDetail.as_view(), name="BookSystemDetail"),
    path('delete/<int:pk>', views.BookDelete.as_view(), name="delete"),
    # path('login', views.Login.as_view(), name="login"),
    # path("logout", views.logoutUser, name="logout"),

]
'''
urlpatterns =[
    path("", views.index, name="index"),
    path("login", views.loginUser, name="login"),
    path("logout", views.logoutUser, name="logout"),
    path("buy/<int:book_id>", views.buy, name="buy"),
    path("delete/<int:book_id>", views.delete, name="delete"),
    path("details/<int:book_id>", views.details, name="details"),


]
'''
