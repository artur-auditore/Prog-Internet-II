from django.urls import path
from .views import *
urlpatterns = [
    path('', ApiRoot.as_view(), name=ApiRoot.name),
    path('profile/', ProfileList.as_view(), name=ProfileList.name),
    path('profile/<int:pk>', ProfileDetail.as_view(), name=ProfileDetail.name),
    path('address/', AddressList.as_view(), name=AddressList.name),
    path('address/<int:pk>', AddressDetail.as_view(), name=AddressDetail.name),
]