from django.urls import path
from . import views

urlpatterns = [
    path('api/', views.APIView.as_view(), name='info')
]