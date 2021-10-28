from django.urls import path, include
from . import views





urlpatterns = [
    path('', views.home, name="home"),
    path('productHdl/',views.productHdl,name='productHdl'),
    path('productHdl/buspro/',views.buspro,name='buspro'),

    
]