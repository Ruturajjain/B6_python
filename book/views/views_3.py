import logging
import re
import traceback

from django.http import HttpResponse
from django.shortcuts import redirect, render

from book.models import Book, Employee

logger = logging.getLogger("first")


# Create your views here.

#for multiple data----request.POST.getlist()
#function based views / class bases views


"""In homepage we add the data of books"""

def homepage(request):                             #request---> http request
    logger.info("In homepage view")
    # print(request.build_absolute_uri())
    # print(request.method)
    # print(request.POST ,type(request.POST))
    # print(request.POST)
    name = request.POST.get("bname")
    price = request.POST.get("bprice")
    qty = request.POST.get("bqty")
    
    if request.method == "POST":
        if not request.POST.get("bid"):
            book_name = name
            book_price = price
            book_qty = qty
            # print(book_name,book_price,book_qty) 
            Book.objects.create(name = book_name, price = book_price, qty = book_qty, )
            return redirect("homepage")
        else:
            bid=request.POST.get("bid")
            try:
                book_obj=Book.objects.get(id = bid)
            except Book.DoesNotExist as err_msg:
                print(err_msg)
            book_obj.name = name
            book_obj.price = price
            book_obj.qty = qty
            book_obj.save()
            return redirect ("show_all_books")
            
    # print(dir(request))
    # a ='[1,5,8,6]'
    # print("in homepage funtion")
    # return HttpResponse("<h3>Hi Hello</h3><h5>Good evening..<h5/>")
    # pass
    
    elif request.method == "GET":
        all_books = Book.objects.all()
        data = {"books": all_books}
        return render(request, template_name = "home1.html",context = data)
        # return render(request,template_name="home1.html")
    


"""Show all books is for showing the records of all books"""
    
def show_all_books(request):
    all_books = Book.objects.all()
    logger.info(f"all data- {all_books}")
    data = {"books": all_books}
    return render(request, template_name = "show_books.html",context = data)


"""we can edit the data of books in via edit button"""
def edit_data(request,id):
    try:
        book = Book.objects.get(id = id)
    except Book.DoesNotExist as err_msg:
        print(err_msg)
    return render (request, template_name = "home1.html", context = {"single_book":book})



"""Delete data is for hard delete a single data from database and all_books"""
def delete_data(request,id):
    if request.method == "POST":
        # print(request.method)
        try:
            book = Book.objects.filter(id = id)
        except Book.DoesNotExist as err_msg:
            traceback.print_exc()
            return HttpResponse(f"Book Does not exist for ID:- {id}")
        else:
            book.delete()
            logger.info(f"Delete book:- {book}")
        return redirect("show_all_books")
    else:
        return HttpResponse(f"Request method- {request.method} not allowed...Only POST method is allowed")


"""via delete_all we can delete all records by one click"""
def delete_all(request):
    all_books = Book.objects.all()
    all_books.delete()
    logger.info(f"all_deleted_books:- {all_books}")
    return render(request, template_name = 'show_books.html')


"""soft delete is only for changing status for book to active or inactive"""
def soft_delete(request,id):
    data = Book.objects.get(id = id)
    data.is_active = 0
    data.save()
    logger.info(f"soft_deleted_book:- {data}")
    return redirect("show_all_books")
    

"""we can see our softdelete data vie this button"""
def show_softdel_data(request):
    all_books = Book.Inactive_objects.all()
    all_data = {"books": all_books}
    return render (request, template_name='softdel.html', context = all_data)
    
    
"""by clicking on restore book status change inactive to active"""
def restore(request,id):
    book = Book.Inactive_objects.get(id = id)
    book.is_active = 1
    book.save()
    return redirect("show_all_books")
    
    
    
def restore_all(request):
    all_books = Book.Inactive_objects.all()
    for book in all_books:
        book.is_active = 1
        book.save()
    return redirect ("show_all_books")

    
    
    
    
    

# assigment 8--
# pep_8 rule follow ,  comments added -- docstring
# using custom model manager
# delete_all_books---delete all books -- all delete
# soft delete button in show_all_book page
# hard delete button in show_all_book_page
# soft delete all
#add page where soft deletes data shown---add button soft_delete_books on home--on this page also make
# button--restore-- and it will recover all data in show_all_books

# logger--5th feb-- integrate with this project
# django debug toolbar -- 



from django.shortcuts import render
from book.forms import AddressForm, Bookform
from django.contrib import messages
# from django.http. response import 

def form_home(request):
    if request.method == 'POST':
        print(request.POST)
        print('in post request')
        form = Bookform(request.POST)
        # print(form.cleaned_data['bname'],'bname')
        if form.is_valid():
            # print(form.cleaned_data['name'])
            form.save()
            messages.success(request, 'data saved successfully!')
            messages.info(request, 'redirecting to home page')
        else:
            messages.error(request, 'Invalid data..')
            
        return redirect("form_home")
        
    elif request.method == 'GET':
        print('in get request')
        context = {"form":Bookform()}
        return render (request, "form_home.html", context)
    else:
        return HttpResponse("invalid http method")


# http methods--get, post, put, delete, patch


# from django.contrib.auth.models import User
# from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# def index(request):
#     user_list = User.objects.all()
#     page = request.GET.get('page', 1)

#     paginator = Paginator(user_list, 10)
#     try:
#         users = paginator.page(page)
#     except PageNotAnInteger:
#         users = paginator.page(1)
#     except EmptyPage:
#         users = paginator.page(paginator.num_pages)

#     return render(request, 'user_list.html', { 'users': users })

from django.views import View

class Homepage(View):
    def get(self, request):
        if request.method == 'GET':
            print('in get request')
            context = {"form":Bookform()}
            return render (request, "form_home.html", context)
        else:
            return HttpResponse('invalid http method')
    
    def post(self, request):
        if request.method == 'POST':
            print(request.POST)
            print('in post request')
            form = Bookform(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'data saved successfully')
            else:
                messages.error(request, 'invalid data')
        return HttpResponse('in post')
    
    def delete(self,request):
        print('in delete request')
        return HttpResponse('in delete')
    
    def put(self, request):
        print('in put request')
        return HttpResponse('in put')
    
    def patch(self, request):
        print('in patch request')
        return HttpResponse('in patch')
       



from django.views.generic.base import TemplateView, RedirectView
class CBVtemplateview(TemplateView):
    extra_context = {'form': Bookform()}
    template_name = 'form_home.html'
    

class CBVtemplateview(RedirectView):
    url = 'homepage'
    
    
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
#generic views


class EmployeeCreate(CreateView):
    model = Employee
    fields = '__all__'
    success_url = reverse_lazy('book:EmployeeRetrieve')          #'http://127.0.0.1:8000/emp-gcreate'
    
    
class EmployeeRetrieve(ListView):  
    model = Employee  
    success_url = reverse_lazy('book:EmployeeRetrieve')
    
    
class EmployeeDetail(DetailView):
    model = Employee
    success_url = reverse_lazy('book:EmployeeDetail')


class EmployeeUpdate(UpdateView):
    model = Employee
    template_name_suffix = '_update_form'
    fields = '__all__'
    success_url = reverse_lazy('book:EmployeeRetrieve')
    
    
class EmployeeDelete(DeleteView):  
    model = Employee  
    template_name_suffix = '_delete'
    success_url = reverse_lazy('book:EmployeeRetrieve') 