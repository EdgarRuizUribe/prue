from django.urls import path
from . import views

urlpatterns = [
    path('', views.store_home, name='store_home'),
    path('storeDetall/<int:pk>/', views.producto_detalle, name='producto_detalle'),
]
