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
