from rest_framework import serializers
from .models import Vessel, History


class VesselSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vessel
        fields = '__all__'


class VesselListSerializer(serializers.ModelSerializer):
    detail_url = serializers.HyperlinkedIdentityField(view_name='detail', lookup_field='pk')
    history = serializers.HyperlinkedIdentityField(view_name='history', lookup_field='pk')

    class Meta:
        model = Vessel
        fields = (
            'detail_url',
            'history',
            'id',
            'code'
        )


class VesselDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vessel
        fields = (
                '__all__'
        )


class HistorySerializer(serializers.ModelSerializer):

    class Meta:
        model = History
        fields = (
            '__all__'
                  )
