from django.utils.translation import gettext_lazy as _
from rest_framework import generics, response, status
from rest_framework_simplejwt.authentication import JWTAuthentication

from ship import serializers
from ship.models import Shipment


class ShipmentList(generics.ListCreateAPIView):
    """Shipment  posts and lists view."""
    queryset = Shipment.objects.all()
    serializer_class = serializers.ShipmentSerializer
    authentication_classes = (JWTAuthentication,)

    def post(self, request, *args, **kwargs):

        serializer = self.serializer_class(data=request.data, context={
            'request': request})
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data,
                                     status=status.HTTP_201_CREATED, )
        return response.Response(serializer.errors,
                                 status=status.HTTP_400_BAD_REQUEST)


class ShipmentDetail(generics.GenericAPIView):
    """Shipment detail."""
    queryset = Shipment.objects.all()
    serializer_class = serializers.ShipmentSerializer
    authentication_classes = (JWTAuthentication,)
    lookup_field = 'uuuid'

    def get(self, request, uuid):
        shipment = Shipment.objects.get(uuid=uuid)
        serializer = self.serializer_class(
            shipment, context={'request': request})
        return response.Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request, uuid):
        shipment = Shipment.objects.get(uuid=uuid)
        if shipment:
            serializer = self.serializer_class(shipment,
                                               data=request.data,
                                               context={'request': request},
                                               partial=True,
                                               )
            if serializer.is_valid():
                serializer.save()
                return response.Response(serializer.data,
                                         status=status.HTTP_201_CREATED, )
        return response.Response(
            {'errors': _(
                'Shipment post with the specified slug does not exist.')},
            status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, uuid):
        try:
            shipment = Shipment.objects.get(uuid=uuid)
            if shipment:
                shipment.delete()
            return response.Response(
                {'message': _('Shipment has been deleted.')},
                status=status.HTTP_200_OK)
        except Shipment.DoesNotExist:
            return response.Response(
                {'message': _('Shipment is not available.')},
                status=status.HTTP_404_NOT_FOUND)




