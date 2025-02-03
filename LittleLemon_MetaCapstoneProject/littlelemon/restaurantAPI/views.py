from django.shortcuts import render, redirect
from rest_framework import generics, viewsets
from rest_framework.decorators import api_view, permission_classes
from .models import Menu, Booking
from .serializers import MenuItemSerializer, BookingSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from .forms import RegisterForm, BookingForm
from django.contrib.auth.models import Group

# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request,'about.html')


# @api_view()
# @permission_classes([IsAuthenticated])
# def msg(request):
#     return Response({'msg':'This view is protected'})

class MenuItemList(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuItemSerializer
    # permission_classes = [IsAuthenticated]
    def get_permissions(self):
        if self.request.method == 'GET':
            self.permission_classes = [AllowAny]
        else:
            self.permission_classes = [IsAuthenticated]
        return super().get_permissions()
    

class MenuItemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuItemSerializer
    # permission_classes = [IsAuthenticated]
    def get_permissions(self):
        if self.request.method == 'GET':
            self.permission_classes = [AllowAny]
        else:
            self.permission_classes = [IsAuthenticated]
        return super().get_permissions()

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]
    

    


    