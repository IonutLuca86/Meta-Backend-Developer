from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('menu/', views.menu, name='menu'),
    path('about/', views.about, name='about'),
    path('menu_db/', views.menu_db, name='menu_db'),
    path('home/', views.home, name='home'),
    path('bookmenu/', views.bookmenu, name='bookmenu'),
    path('bookabout/', views.bookabout, name='bookabout'),
    path('book/', views.book, name='book'),
]