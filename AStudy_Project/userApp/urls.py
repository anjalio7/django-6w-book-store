from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('login', views.login_view, name = 'logins'),
    path('register', views.register, name = 'register'),
    path('logout', views.logout_view, name = 'logout'),
    path('getSubCat/<int:id>', views.getSubCat, name = 'getSubCat'),
    path('viewBook/<int:id>', views.viewBook, name = 'viewBook'),
    path('detailBook/<int:id>', views.detailBook, name = 'detailBook'),
    path('createOrder/<int:id>', views.createOrder, name = 'createOrder'),
    path('allOrders', views.allOrders, name = 'allOrders'),
]