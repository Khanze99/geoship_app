from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from .models import Vessel, History
from .serializers import VesselListSerializer, VesselDetailSerializator, HistorySerializer
from django.contrib.auth.models import User

# Create your views here.


class ApiInfo(APIView):
    def get(self, request, format=None):
        return Response(data={'API': 'Welcome to the service'})


class VesselDetailAPIView(RetrieveAPIView):
    serializer_class = VesselDetailSerializator
    queryset = Vessel.objects.all()


class ListVesselsAPI(ListAPIView):
    serializer_class = VesselListSerializer

    def get_queryset(self):
        queryset = Vessel.objects.all()
        return queryset

    # def get_queryset(self):
    #     user = User.objects.get(id=self.kwargs['uid'])
    #     queryset_list = Vessel.objects.filter(owner=user)
    #     if user.is_staff:
    #         queryset_list = Vessel.objects.all()
    #     return queryset_list


class HistoryAPI(ListAPIView):
    serializer_class = HistorySerializer

    def get_queryset(self):
        vessel = Vessel.objects.get(id=self.kwargs['pk'])
        queryset = History.objects.filter(vessel=vessel)
        return queryset
