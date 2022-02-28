from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Book
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views import View
from django.views.generic import TemplateView
from .forms import BookCreation
from django.core.paginator import Paginator
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
class BookCreate(LoginRequiredMixin, CreateView):
    form_class = BookCreation
    template_name = 'bookmanagement/book_form.html'

    def get_success_url(self):
        return reverse("book")

    def form_valid(self, form):
        price = form.cleaned_data.get("unitprice")
        stock = form.cleaned_data.get("in_stock")
        BookCreate.totalprice = price * stock
        return super(BookCreate, self).form_valid(form)




class BookRetrieve(ListView):
    model: Book
    template_name = 'bookmanagement/book_list.html'

    def get_queryset(self):
        queryset = Book.objects.all()
        paginator = Paginator(queryset, 15)
        page_number = self.request.GET.get('page')
        object_list = paginator.get_page(page_number)
        return object_list


class BookDetail(DetailView):
    model: Book
    template_name = 'bookmanagement/book_detail.html'

    # queryset = Book.objects.all()  itis writren then we need to pass id as pk in url and delete get_object method

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Book, id=id_)


class BookUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "bookmanagement/book_update.html"
    form_class = BookCreation
    queryset = Book.objects.all()

    def get_success_url(self):
        return reverse("book")


class BookDelete(LoginRequiredMixin, DeleteView):
    template_name = "bookmanagement/book_confirm_delete.html"
    queryset = Book.objects.all()

    def get_success_url(self):
        return reverse("book")


class List(TemplateView):
    template_name = 'bookmanagement/book_list.html'

    def get_context_data(self, request, **kwargs):
        all_books = Book.objects.all()

        context = {
            'object_list': all_books,

        }
        return context


class BookList(View):

    def get(self, request):
        all_books = Book.objects.all()
        paginator = Paginator(all_books, 2)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, 'bookmanagement/book_list.html', {'page_obj': page_obj})


class BookSystemDetail(View):
    def get(self, request):
        form = BookCreation()
        return render(request, 'bookmanagement/book_form.html', {'form': form})

    def post(self, request):
        form = BookCreation(request.POST, request.FILES)
        if form.is_valid():
            return HttpResponse("Wecome")
        else:
            form = BookCreation()
        return render(request, 'bookmanagement/book_form.html', {'form': form})


'''

def index(request):
    all_collegebook = Book.objects.all()
    return render(request, 'book_list.html', {'books': all_collegebook})
'''


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


'''
@login_required
def buy(request, book_id):
    book = Book.objects.get(id=book_id)
    if book.in_stock == 0 :
        print("out of stock")
    else:
        newstock = book.in_stock -1
        book.in_stock= newstock
        book.save()
'''

'''
def delete(request, book_id):
    book = Book.objects.get(id=book_id)
    if book.delete() is None:
        messages.warning(request, "failed to delete")
    else:
        messages.success(request, "book deleted successfully")
    return redirect('index')
'''


def details(request, book_id):
    book = Book.objects.filter(id=book_id)
    return render(request, 'bookmanagement/book_detail.html', {'books': book})


'''
class Login(View):
    def get(self, request):
        return render(request, 'registration/login.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            messages.warning(request, "please enter correct username and password")
            return render(request, "registration/login.html")
'''

'''
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

'''

'''
def logoutUser(request):
    logout(request)
    return redirect("/login")
'''
