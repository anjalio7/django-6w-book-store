from django.urls import path,include
from . import views
urlpatterns = [
    path('indexx' , views.layout , name = "indexx"),
    path('login', views.login_view, name = "login"),
    path('logout', views.logout_view, name = "logout"),
    path('addc' , views.addCategory, name= "addc"),
    path('allCategory', views.allCategory, name = "allCategory"),
    path('editCategory/<int:ids>', views.editCategory, name="editCategory"),
    path('deleteCategory/<int:ids>', views.deleteCategory, name="deleteCategory"),
    path('subC', views.subCategory, name="subC"),
    path('subCategory', views.subCat, name= "subCategory"),
    path('editSub/<int:ids>', views.editSub, name= "editSub"),
    path('delete-subCategory/<int:ids>', views.deleteSubCategory, name= "delete-subCategory"),
    path('book', views.addBook, name= "book"),
    path('allBook', views.allBooks, name= "allBook"),
    path('deleteBook/<int:id>', views.deleteBook, name= "deleteBook"),
    path('editBook/<int:id>', views.editBook, name= "editBook"),
    path('viewOrders', views.viewOrders, name= "viewOrders"),
    path('updateOrder/<int:id>/<str:type>', views.updateOrder, name= "updateOrder"),
    
]

