from django.urls import path

from .views import (
    UserListCreate, UserRetrieveUpdateDelete,
    ServiceRefListCreate, ServiceRefRetrieveUpdateDelete,
    ServiceListCreate, ServiceRetrieveUpdateDelete,
    ServiceReviewsListCreate, ServiceReviewsRetrieveUpdateDelete,
    BookingListCreate, BookingRetrieveUpdateDelete, EntryPoint
)

urlpatterns = [
    path('', EntryPoint.as_view(), name='entry-point'),
    
    path('users', UserListCreate.as_view(), name='user-list-create'),
    path('users/<int:pk>', UserRetrieveUpdateDelete.as_view(), name='user-detail'),

    path('service-refs', ServiceRefListCreate.as_view(), name='service-ref-list-create'),
    path('service-refs/<int:pk>', ServiceRefRetrieveUpdateDelete.as_view(), name='service-ref-detail'),

    path('services', ServiceListCreate.as_view(), name='service-list-create'),
    path('services/<int:pk>', ServiceRetrieveUpdateDelete.as_view(), name='service-detail'),

    path('service-reviews', ServiceReviewsListCreate.as_view(), name='service-reviews-list-create'),
    path('service-reviews/<int:pk>', ServiceReviewsRetrieveUpdateDelete.as_view(), name='service-reviews-detail'),

    path('bookings/', BookingListCreate.as_view(), name='booking-list-create'),
    path('bookings/<int:pk>', BookingRetrieveUpdateDelete.as_view(), name='booking-detail'),
]