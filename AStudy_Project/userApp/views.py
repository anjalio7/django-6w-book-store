from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.core.exceptions import ValidationError

from django.contrib.auth.decorators import login_required

from adminApp.models import user, category, subcategory, book, order
# Create your views here.
def index(request):
    catData = category.objects.all()
    return render(request, 'userApp/index.html', {'catData': catData})

def login_view(request):
    if request.method == "POST":
        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username,
        password=password)
        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "userApp/login.html", {
            "message": "Invalid username and/or password."
        })
    else:
        return render(request, "userApp/login.html")

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "userApp/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            users = user.objects.create_user(username, email, password)
            users.save()
        except IntegrityError:
            return render(request, "userApp/register.html", {
                "message": "Username already taken."
            })
        # return render(request, 'userApp/register.html', {"message": 'Registered successfully.'})
        return HttpResponseRedirect(reverse('login'))
    else:
        return render(request, "userApp/register.html")


def getSubCat(request, id):
    catData = category.objects.get(id = id)
    subData = subcategory.objects.filter(category_id = catData)
    return render(request, 'userApp/subCat.html', {'sub': subData})

def viewBook(request, id):
    subData = subcategory.objects.get(id = id)
    bookData = book.objects.filter(subcategory_id = subData)
    return render(request, 'userApp/viewBook.html', {'bData': bookData})

def detailBook(request, id):
    data = book.objects.get(id = id)
    return render(request, 'userApp/detailBook.html', {'data': data})

@login_required(login_url='/login')
def createOrder(request, id):
    orderBook = book.objects.get(id = id)
    fetchOrder = order.objects.filter(user_id = request.user, book_id = orderBook)
    if len(fetchOrder) > 0:
        return render(request, 'userApp/detailBook.html', {'data': orderBook, 'msg': 'Book is already ordered.'})
    else:
        if orderBook.stock > 0:
            if request.method == 'POST':
                quant = request.POST['quan']
                address = request.POST['address']

                total = int(quant) * int(orderBook.price)

                a = order(user_id = request.user, book_id = orderBook, quantity = quant, address = address, total_amount = total)
                a.save()
                return render(request, 'userApp/order.html', {'data': orderBook})
            else:
                return render(request, 'userApp/order.html', {'data': orderBook})
        else:
            return render(request, 'userApp/detailBook.html', {'data': orderBook, 'msg': 'Stock not available'})

@login_required(login_url='/login')
def allOrders(request):
    data = order.objects.filter(user_id = request.user)
    return render(request, 'userApp/allOrder.html', {'data': data})
