from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register(r'vessels', views.VesselAPIViewSet, basename='vessel')

urlpatterns = []

urlpatterns += router.urls

