from django.urls import path
from . import views

urlpatterns = [
    path('', views.ApiInfo.as_view(), name='info'),
    path('list/', views.ListVesselsAPI.as_view(), name='list'),
    path('vessel/<int:pk>/', views.VesselDetailAPIView.as_view(), name='detail'),
    path('vessel/<int:pk>/history/', views.HistoryAPI.as_view(), name='history')
]