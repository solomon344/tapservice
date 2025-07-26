from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView,  RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from Serializers.serializers import (UserSerializer, ServiceRefSerializer, ServiceSerializer, ServiceReviewsSerializer, BookingSerializer)
from .models import (ServiceRef, Service, ServiceReviews, Booking)
from django.contrib.auth import get_user_model
from django_filters.rest_framework.backends import DjangoFilterBackend


# Create your views here.
User = get_user_model()

class UserListCreate(ListCreateAPIView):
    """
    <h3>API view for listing and creating User instances. </h3>
    \n
    This view provides GET and POST methods for the User model.\n

    - **GET**: Returns a list of all User objects. \n
    - **POST**: Creates a new User object. \n
    """
    
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserRetrieveUpdateDelete(RetrieveUpdateDestroyAPIView):
    """
    <h3>API view for retrieving, updating, and deleting User instances. </h3>
    \n
    This view provides GET, PUT, and DELETE methods for the User model.\n

    - **GET**: Returns a User object. \n
    - **PUT**: Updates a User object. \n
    - **DELETE**: Deletes a User object. \n
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ServiceRefListCreate(ListCreateAPIView):
    """
    <h3>API view for listing and creating ServiceRef instances. </h3>
    \n
    This view provides GET and POST methods for the ServiceRef model.\n

    - **GET**: Returns a list of all ServiceRef objects. \n
    - **POST**: Creates a new ServiceRef object. \n
    """
    queryset = ServiceRef.objects.all()
    serializer_class = ServiceRefSerializer

class ServiceRefRetrieveUpdateDelete(RetrieveUpdateDestroyAPIView):
    """
    <h3>API view for retrieving, updating, and deleting ServiceRef instances. </h3>
    \n
    This view provides GET, PUT, and DELETE methods for the ServiceRef model.\n

    - **GET**: Returns a ServiceRef object. \n
    - **PUT**: Updates a ServiceRef object. \n
    - **DELETE**: Deletes a ServiceRef object. \n
    """
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
    
    - **Example Request**: GET /api/services/?service_ref__name=Cleaning
    - **Example Response**:
     
     [
        {
        "id": 1,
        "service_ref": 1,
        "user": 1,
        "bookings": []
        }
     ]
     

    """

    
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['service_ref__name', 'bookings__status','user']

class ServiceRetrieveUpdateDelete(RetrieveUpdateDestroyAPIView):
    """
    <h3>API view for retrieving, updating, and deleting Service instances. </h3>
    \n
    This view provides GET, PUT, and DELETE methods for the Service model.\n

    - **GET**: Returns a Service object. \n
    - **PUT**: Updates a Service object. \n
    - **DELETE**: Deletes a Service object. \n
    """
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

class ServiceReviewsListCreate(ListCreateAPIView):
    """
    <h3>API view for listing and creating ServiceReviews instances. </h3>
    \n
    This view provides GET and POST methods for the ServiceReviews model.\n

    - **GET**: Returns a list of all ServiceReviews objects. \n
    - **POST**: Creates a new ServiceReviews object. \n
     """
    queryset = ServiceReviews.objects.all()
    serializer_class = ServiceReviewsSerializer

class ServiceReviewsRetrieveUpdateDelete(RetrieveUpdateDestroyAPIView):
    """
    <h3>API view for retrieving, updating, and deleting ServiceReviews instances. </h3>
    \n
    This view provides GET, PUT, and DELETE methods for the ServiceReviews model.\n

    - **GET**: Returns a ServiceReviews object. \n
    - **PUT**: Updates a ServiceReviews object. \n
    - **DELETE**: Deletes a ServiceReviews object. \n
    """
    queryset = ServiceReviews.objects.all()
    serializer_class = ServiceReviewsSerializer

class BookingListCreate(ListCreateAPIView):
    """
    <h3>API view for listing and creating Booking instances. </h3>
    \n
    This view provides GET and POST methods for the Booking model.\n

    - **GET**: Returns a list of all Booking objects. \n
    - **POST**: Creates a new Booking object. \n
    """
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

class BookingRetrieveUpdateDelete(RetrieveUpdateDestroyAPIView):
    """
    <h3>API view for retrieving, updating, and deleting Booking instances. </h3>
    \n
    This view provides GET, PUT, and DELETE methods for the Booking model.\n

    - **GET**: Returns a Booking object. \n
    - **PUT**: Updates a Booking object. \n
    - **DELETE**: Deletes a Booking object. \n
    """
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
    
