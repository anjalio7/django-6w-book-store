from sqlite3 import IntegrityError
from django.shortcuts import render , reverse
from django.http import HttpResponse , HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from .models import user, category, subcategory, book, order

from django.db import IntegrityError

from . import models

# Create your views here.
def layout(request):
    catCount = category.objects.all().count()
    subCatCount = subcategory.objects.all().count()
    bookCount = book.objects.all().count()
    orderCount = order.objects.all().count()
    return render(request , 'adminApp/home.html', {'catCount': catCount, 'subCount': subCatCount, 'bookCount': bookCount, 'orderCnt': orderCount})


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
            return HttpResponseRedirect(reverse("indexx"))
        else:
            return render(request, "adminApp/login.html", {
            "message": "Invalid username and/or password."
        })
    else:
        return render(request, "adminApp/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))

#start category    

def addCategory(request):
    if request.method == "POST":
        catName = request.POST['name']
        try:
            a = category(category_name = catName)
            a.save()
            return HttpResponseRedirect(reverse('allCategory'))
        except  IntegrityError:
            print('hey')
            return render(request, 'adminApp/addCategory.html', {'msg': 'Category already exists.'})
    else:
        return render(request , 'adminApp/addCategory.html') 
    
def editCategory(request,ids):
    category = models.category.objects.get(id=ids)
    if request.method == "POST":
        edCat = request.POST['name']
        try:
            category.category_name = edCat
            category.save()
            return HttpResponseRedirect(reverse('allCategory'))
        except IntegrityError:
            return render(request , 'adminApp/editCategory.html', {'data': category, 'msg': 'Category already exists.'})
    else:
        return render(request , 'adminApp/editCategory.html', {'data': category})

def deleteCategory(request,ids):
        cat = models.category.objects.get(id=ids)
        cat.delete()
        return HttpResponseRedirect(reverse('allCategory'))


def allCategory(request):
    allCat = category.objects.all()
    return render(request, 'adminApp/viewCategory.html', {'data': allCat}) 

#start subcategory     

def subCategory(request):
    categories = models.category.objects.all()
    print(category)
    if request.method == "POST":
        subName = request.POST['name']
        catId = request.POST['category_Name']
        # print (subName,catId)
        selCat = category.objects.get(id = catId)
        img = request.FILES['image']
        # catId = request.POST['id']
        try:
            a = subcategory(category_id = selCat, category_name = subName, image = img)
            a.save()
            return HttpResponseRedirect(reverse("subCategory"))
        except:
            return render(request, 'adminApp/subCategory.html', {'data': categories, 'msg': 'Subcategory already exists.'})
    else:
        return render(request , 'adminApp/subCategory.html', {'data':categories}) 


def editSub(request,ids):
    categories = models.category.objects.all()
    data = models.subcategory.objects.get(id = ids)
    if request.method == "POST":
        subName = request.POST['name']
        catId = request.POST['category_Name']
        selCat = category.objects.get(id = catId)
        img = request.FILES.get('image')
        if img is not None:
            data.image = img
        try:
            # a = subcategory(category_id = selCat, category_name = subName)
            # a.save()
            data.category_id = selCat
            data.category_name = subName
            data.save()
            return HttpResponseRedirect(reverse("subCategory"))
        except:
            return render(request, 'adminApp/subCategory.html', {'data': categories, 'msg': 'Subcategory already exists.'})
    else:
        return render(request , 'adminApp/editSub.html', {'data': categories, 'sub': data})

def deleteSubCategory(request,ids):
        dele = models.subcategory.objects.get(id=ids)
        dele.delete()
        return HttpResponseRedirect(reverse('subCategory'))

def subCat(request):
    subCate = subcategory.objects.all()
    return render(request, 'adminApp/viewSub.html', {'data': subCate}) 

#start books content
#def book(request):
    #book = models.book.objects.all()
    #subid= models.
    #return render(request, 'adminApp/book.html',{'data': book})

def addBook(request):
    subcatId = models.subcategory.objects.all()
    print(subcatId)
    if request.method == 'POST':
        subcat = request.POST['subcategory_ids']
        selsubcat = models.subcategory.objects.get(id = subcat)
        name = request.POST['name']
        pubyear = request.POST['Publication Year']
        pub = request.POST['Publication']
        author = request.POST['Author']
        price = request.POST['Price']
        desc = request.POST['desc']
        img = request.FILES['image']
        stock = request.POST['stock']
        a = models.book(subcategory_id= selsubcat , name= name, publication_year= pubyear, publication= pub, author= author, price= price, img = img, description = desc, stock = stock )
        a.save()
        # return render(request,'adminApp/addBook.html')
        return HttpResponseRedirect(reverse('allBook'))
    else:
        return render(request,'adminApp/addBook.html', {'data': subcatId})

def allBooks(request):
    books = models.book.objects.all()
    return render(request, 'adminApp/viewBooks.html', {'data': books})

def deleteBook(request, id):
    data = models.book.objects.get(id = id)
    data.delete()
    return HttpResponseRedirect(reverse('allBook'))


def editBook(request, id):
    data = models.book.objects.get(id = id)
    subcatId = models.subcategory.objects.all()
    if request.method == 'POST':
        subcat = request.POST['subcategory_ids']
        selsubcat = models.subcategory.objects.get(id = subcat)
        name = request.POST.get('name')
        pubyear = request.POST['Publication Year']
        pub = request.POST['Publication']
        author = request.POST['Author']
        price = request.POST['Price']
        desc = request.POST['desc']
        img = request.FILES.get('image')
        stock = request.POST['stock']
        if img is not None:
            data.img = img
        
        data.subcategory_id = selsubcat
        data.name = name
        data.publication_year = pubyear
        data.publication = pub
        data.author = author
        data.price = price
        data.description = desc
        data.stock = stock
        data.save()
        return HttpResponseRedirect(reverse('allBook'))
    else:
        return render(request,'adminApp/editBook.html', {'data': subcatId, 'book': data})


def viewOrders(request):
    data = order.objects.all()
    return render(request, 'adminApp/listOrder.html', {'data': data})


def updateOrder(request, id, type):
    orderData = order.objects.get(id = id)
    orderData.status = type
    orderData.save()
    if type == 'Accept':
        books = book.objects.get(id = orderData.book_id.id)
        # print(f'books is {books}')
        books.stock = int(books.stock) - int(orderData.quantity)
        books.save()
    return HttpResponseRedirect(reverse('viewOrders'))