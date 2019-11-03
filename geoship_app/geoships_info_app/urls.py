from django.urls import path
from . import views

urlpatterns = [
    path('', views.ApiInfo.as_view(), name='info'),
    path('list/', views.ListVesselsAPI.as_view(), name='list'),
    path('vessel/<int:id>/', views.VesselDetailAPIView.as_view(), name='detail')
]