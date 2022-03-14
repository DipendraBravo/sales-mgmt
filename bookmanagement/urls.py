from django.urls import path
from . import views

urlpatterns = [
    # path('', views.BookRetrieve.as_view(), name="book"),

     # path('buy', views.BuyFunction.as_view(), name="book"),
    path('',views.BookList.as_view(), name='book'),
    path('create/', views.BookCreate.as_view(), name="book_create"),
    path('search', views.SearchedView.as_view(), name="search"),
    path('buy', views.UpdateBuyView.as_view(), name="buy"),
    # path('test',views.TestView.as_view(),name="test"),
    path('user', views.UserList.as_view(), name="user"),
    path('bookrequest', views.BookRequestList.as_view(), name="bookrequest"),
    path('searchedrequest', views.SearchRequestList.as_view(), name="searchedrequest"),
     path('purchased/<int:book_id>', views.PurchasedBookView.as_view(), name="purchased"),
    # path('updatebuy/<int:pk>)', views.UpdateBuyFunction.as_view(), name="update"),
    path('<int:id>', views.BookDetail.as_view(), name="BookDetail"),
    path('<int:pk>/bookrequestupdate/', views.BookRequestEdit.as_view(), name="bookrequestedit"),
    path('<int:pk>/update/', views.BookUpdateView.as_view(), name="BookUpdate"),
    path('<int:pk>/delete/', views.BookDelete.as_view(), name="BookDelete"),
    # path('detail/<int:book_id>', views.BookSystemDetail.as_view(), name="BookSystemDetail"),
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
