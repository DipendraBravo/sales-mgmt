from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Book
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


# Create your views here.

def index(request):
    all_college = Book.objects.all()
    return render(request, 'index.html', {'books': all_college})


@login_required
def buy(request, book_id):
    book = Book.objects.get(id=book_id)
    new = 0 if book.in_stock == 0 else -1
    if new == 0:
        messages.warning(request, "Out of Stock")
        return redirect('index')
    book.in_stock += new
    book.save()
    if book.id is not None:
        messages.success(request, "Book purchased successfully")
    else:
        messages.warning(request, "Oops something went wrong")
    return redirect('index')


def delete(request, book_id):
    book = Book.objects.get(id=book_id)
    if book.delete() is None:
        messages.warning(request, "failed to delete")
    else:
        messages.success(request, "book deleted successfully")
    return redirect('index')


def loginUser(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')


        # check if user has entered correct credentials
        user = authenticate(username=username, password=password)

        if user is not None:
            # A backend authenticated the credentials
            login(request, user)
            return redirect("/")

        else:
            messages.warning(request, "please enter correct username and password")
            return render(request, 'login.html')

    return render(request, 'login.html')


def logoutUser(request):
    logout(request)
    return redirect("/login")
