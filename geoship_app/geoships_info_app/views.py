from rest_framework.viewsets import ViewSet
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from .models import Vessel, History
from .serializers import HistorySerializer, VesselSerializer
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist


class VesselAPIViewSet(ViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = VesselSerializer

    def list(self, request):
        user = User.objects.get(id=self.request.user.id)
        try:
            queryset = Vessel.objects.filter(owner=user)
        except ObjectDoesNotExist:
            queryset = []
        if user.is_staff:
            queryset = Vessel.objects.all()
        serializer = self.serializer_class(data=queryset, many=True)
        serializer.is_valid()
        return Response(serializer.data)


class HistoryAPI(ListAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = HistorySerializer

    def get_queryset(self):
        user_id = self.request.user.id
        user = User.objects.get(id=user_id)
        vessel = Vessel.objects.get(id=self.kwargs['id'])
        if user.is_staff:
            queryset = History.objects.filter(vessel=vessel)
            return queryset
        try:
            if vessel.owner.id == user_id:
                queryset = History.objects.filter(vessel=vessel)
                return queryset
        except AttributeError:
            return []
        return []
