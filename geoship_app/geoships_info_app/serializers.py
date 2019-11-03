from rest_framework import serializers
from .models import Vessel


class VesselSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vessel
        fields = (
            'id',
            'name'
        )


class VesselDetailSerializator(serializers.ModelSerializer):
    class Meta:
        model = Vessel
        fields = (
                '__all__'
        )
