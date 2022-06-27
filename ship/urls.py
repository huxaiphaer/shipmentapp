from django.urls import path

from . import views

urlpatterns = [
    path('', views.ShipmentList.as_view(), name='shipment'),
    path('<uuid:uuid>/',
         views.ShipmentDetail.as_view(), name='shipment-detail'),
]
