from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from .models import Vessel
from .serializers import VesselSerializer, VesselDetailSerializator
from django.contrib.auth.models import User

# Create your views here.


class ApiInfo(APIView):
    def get(self, request, format=None):
        return Response(data={'API': 'Welcome to the service'})


class VesselDetailAPIView(RetrieveAPIView):
    serializer_class = VesselDetailSerializator
    queryset = Vessel.objects.all()


class ListVesselsAPI(ListAPIView):
    serializer_class = VesselSerializer

    def get_queryset(self):
        queryset = Vessel.objects.all()
        return queryset

    # def get_queryset(self):
    #     user = User.objects.get(id=self.kwargs['uid'])
    #     queryset_list = Vessel.objects.filter(owner=user)
    #     if user.is_staff:
    #         queryset_list = Vessel.objects.all()
    #     return queryset_list
