from rest_framework.serializers import (ModelSerializer, HyperlinkedModelSerializer, HyperlinkedRelatedField)
from django.contrib.auth import get_user_model
from authentication.models import User
from api.models import (ServiceRef, Service, ServiceReviews, Booking)


class ServiceRefSerializer(ModelSerializer):

    class Meta:
        model = ServiceRef
        fields = ['id', 'name', 'description', 'cover_image', 'icon', 'created_at', 'updated_at']
        read_only_fields = ['id']


class ServiceReviewsSerializer(ModelSerializer):
    by = HyperlinkedRelatedField(view_name='user-detail', read_only=True)
    class Meta:
        model = ServiceReviews
        fields = ['id', 'service', 'rate', 'comment', 'by', 'created_at', 'updated_at']
        read_only_fields = ['id']

class BookingSerializer(ModelSerializer):
    class Meta:
        model = Booking
        fields = ['id', 'service', 'user', 'date', 'time', 'address', 'status']
        read_only_fields = ['id']


class ServiceSerializer(ModelSerializer):
    service_ref = ServiceRefSerializer(read_only=True)
    bookings = BookingSerializer(many=True, read_only=True)
    class Meta:
        model = Service
        fields = ['id', 'service_ref', 'user', 'cover_image', 'created_at', 'updated_at','bookings']
        read_only_fields = ['id']
        

class UserSerializer(ModelSerializer):
    services = ServiceSerializer(many=True, read_only=True)
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'picture', 'phone','services']
        read_only_fields = ['id']


