from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView,  RetrieveUpdateDestroyAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from Serializers.serializers import (UserSerializer, ServiceRefSerializer, ServiceSerializer, ServiceReviewsSerializer, BookingSerializer)
from .models import (ServiceRef, Service, ServiceReviews, Booking)
from django.contrib.auth import get_user_model

# Create your views here.
User = get_user_model()

class UserListCreate(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserRetrieveUpdateDelete(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ServiceRefListCreate(ListCreateAPIView):
    queryset = ServiceRef.objects.all()
    serializer_class = ServiceRefSerializer

class ServiceRefRetrieveUpdateDelete(RetrieveUpdateDestroyAPIView):
    queryset = ServiceRef.objects.all()
    serializer_class = ServiceRefSerializer

class ServiceListCreate(ListCreateAPIView):
    """
    <h3>API view for listing and creating Service instances. </h3>
    \n
    This view provides GET and POST methods for the Service model.\n

    - **GET**: Returns a list of all Service objects, with optional filtering. \n
    - **POST**: Creates a new Service object. \n

    <h3>Filtering</h3>
    \n
    You can filter the list of services using the following fields: \n
    - **service_ref__name**: Filter services by the name of the related service reference. \n
    - **bookings__status**: Filter services by the status of related bookings. \n
    - **user**: Filter services by the associated user.
    """

    
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['service_ref__name', 'bookings__status','user']

class ServiceRetrieveUpdateDelete(RetrieveUpdateDestroyAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

class ServiceReviewsListCreate(ListCreateAPIView):
     
    queryset = ServiceReviews.objects.all()
    serializer_class = ServiceReviewsSerializer

class ServiceReviewsRetrieveUpdateDelete(RetrieveUpdateDestroyAPIView):
    queryset = ServiceReviews.objects.all()
    serializer_class = ServiceReviewsSerializer

class BookingListCreate(ListCreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

class BookingRetrieveUpdateDelete(RetrieveUpdateDestroyAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

class EntryPoint(APIView):
    """
    <h3>Introduction </h3>Welcome to the TapService API. Use the endpoints to manage users, services, and bookings.\n
    This view serves as the entry point for the API, providing a brief overview of available endpoints.
    \n

    <h3> Resource Endpoints</h3> \n
    - <strong>users</strong>: /api/users \n
    - <strong>service_refs</strong>: /api/service-refs \n
    - <strong>services</strong>: /api/services \n
    - <strong>service_reviews</strong>: /api/service-reviews \n
    - <strong>bookings</strong>: /api/bookings \n
    \n
     <h3> Authentication Endpoints</h3> \n
     \n
     <h4>Token Auth</h4>
     - <strong>Access Token</strong>: BASE_URL/auth/access -> Access Token \n
     - <strong>Refresh Token</strong>: BASE_URL/auth/refresh  -> Refresh & Access Token \n
    """
    permission_classes = [AllowAny]
    
    def get(self, request, *args, **kwargs):
        return Response({
            "message": "Welcome to the TapService API. Use the endpoints to manage users, services, and bookings.",
            "endpoints": {
                "users": "/api/users/",
                "service_refs": "/api/service-refs/",
                "services": "/api/services/",
                "service_reviews": "/api/service-reviews/",
                "bookings": "/api/bookings/"
            }
        })
    
