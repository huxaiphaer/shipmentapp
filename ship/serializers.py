from rest_framework import serializers

from ship.models import Shipment


class ShipmentSerializer(serializers.Serializer):
    """
    Shipment Serializer Class.
    """

    class Meta:
        model = Shipment
        fields = ('package_name', 'shipping_date', 'arrival_date',
                  'status', 'country_of_origin', 'destination_country',)
        readonly = ('uuid',)

    def create(self, validated_data):
        shipment = Shipment.objects.create(**validated_data,
                                           user=self.context['request'].user)
        return shipment

    def update(self, instance, validated_data):
        pass

