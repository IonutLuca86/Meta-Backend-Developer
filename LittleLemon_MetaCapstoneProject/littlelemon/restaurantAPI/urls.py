from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register('tables', views.BookingViewSet, basename='booking')

urlpatterns = [
    path('', views.index, name='home'),
    path('about/',views.about, name='about'),
    path('restaurant/menu/', views.MenuItemList.as_view(), name='menu'),
    path('restaurant/menu/<int:pk>/', views.MenuItemDetail.as_view(), name='menu-detail'),   
    path('restaurant/booking/', include(router.urls)),
    path('api-token-auth/', obtain_auth_token),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
]