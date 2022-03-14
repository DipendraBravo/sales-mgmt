from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Book, UserRequest
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, DeleteView, UpdateView, FormView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views import View
from django.views.generic import TemplateView
from .forms import BookCreation, UserRequestForm
from django.core.paginator import Paginator
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
class SearchRequestList(ListView):
    model = UserRequest
    template_name = "bookmanagement/searchedrequest_list.html"

    def get_queryset(self):
        search = self.request.GET.get('status')
        queryset = UserRequest.objects.filter(delivered_status__icontains=search)
        return queryset


class BookRequestEdit(UpdateView):
    model = Book
    form_class = UserRequestForm
    queryset = UserRequest.objects.all()
    template_name = "bookmanagement/bookrequest_update.html"

    def get_success_url(self):
        return reverse('book')

    def _update_delivered(self, forms, user_req):
        book = forms['book'].value()
        book_obj = Book.objects.filter(pk=book).first()
        date_check = ((user_req.updated_at - user_req.created_at).seconds == 0)
        requested_quantity = forms['book_quantity'].value()
        stock_check = (book_obj.in_stock - int(requested_quantity)) >= 0
        if stock_check and date_check:
            book_obj.in_stock -= abs(int(requested_quantity))
            book_obj.save()
            forms.save()

    def post(self, request, pk, *args, **kwargs):
        user_request_obj = UserRequest.objects.get(pk=pk)
        forms = UserRequestForm(request.POST)
        is_delivered = forms['delivered_status'].value()

        if is_delivered == "delivered":
            status = self._update_delivered(forms,user_request_obj)

        return render(request, "bookmanagement/bookrequest_list.html")

'''
    def form_valid(self, form):
        qty = form.cleaned_data.get("book_quantity")
        status = form.cleaned_data.get("delivered_Status")
        self.book.in_stock = qty
        breakpoint()
        if status == 'delivered':
            pass
        else:
            pass
        return super(BookRequestEdit, self).form_valid(form)
        pass
'''


class UserList(ListView):
    model = User
    template_name = "bookmanagement/user_list.html"

    def get_queryset(self):
        queryset = User.objects.all()
        return queryset


class BookRequestList(ListView):
    model = UserRequest
    template_name = "bookmanagement/bookrequest_list.html"

    def get_queryset(self):
        queryset = UserRequest.objects.all()
        return queryset


class PurchasedBookView(View):
    def get(self, request, book_id):
        form = UserRequestForm
        book = Book.objects.get(id=book_id)
        context = {
            "book": book,
            "form": form
        }
        return render(request, 'bookmanagement/purchased_detail.html', context)

    def post(self, request, book_id):
        form = UserRequestForm
        books = Book.objects.get(id=book_id)
        context = {
            "book": books,
            "form": form
        }
        form = UserRequestForm(request.POST)
        if form.is_valid():
            form.instance.book = books
            form.save()
            return redirect('book')
        else:
            return render(request, 'bookmanagement/purchased_detail.html', context)


class TestView(CreateView):
    model = UserRequest
    form_class = UserRequestForm
    template_name = 'bookmanagement/purchased_detail.html'


class SearchedView(ListView):
    model = Book
    template_name = 'bookmanagement/searched_list.html'

    def get_queryset(self):
        search = self.request.GET.get('searched')
        query = Book.objects.filter(book_name__icontains=search)
        paginator = Paginator(query, 15)
        page_number = self.request.GET.get('page')
        object_list = paginator.get_page(page_number)
        return object_list


class UpdateBuyView(UpdateView):
    model = Book
    queryset = Book.objects.all()
    fields = []
    obj: Book

    def get_success_url(self):
        return reverse('book')

    def post(self, request, **kwargs):
        self.get_object(request.POST.get('book_id'))
        self.obj.in_stock -= abs(int(request.POST.get('in_stock')))
        if self.obj.in_stock >= 0:
            self.obj.totalprice = self.obj.unitprice * self.obj.in_stock
            self.obj.save()
            messages.success(request, "order placed successfully")
        else:
            messages.warning(request, "failed to placed order")
        return redirect('book')

    def get_object(self, id):
        self.obj = get_object_or_404(Book, id=id)


'''
class UpdateBuyFunction(View):
    def get_object(self, id):
        print(id)
        return Book.objects.get(pk=id)

    def get(self, request, id):
        pass

'''


class BookCreate(LoginRequiredMixin, CreateView):
    form_class = BookCreation
    template_name = 'bookmanagement/book_form.html'

    def get_success_url(self):
        return reverse("book")

    def form_valid(self, form):
        price = form.cleaned_data.get("unitprice")
        stock = form.cleaned_data.get("in_stock")
        form.instance.totalprice = price * stock
        return super(BookCreate, self).form_valid(form)


class BookList(ListView):
    form_class = BookCreation
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


'''
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

'''
def details(request, book_id):
    book = Book.objects.filter(id=book_id)
    return render(request, 'bookmanagement/book_detail.html', {'books': book})



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
'''
