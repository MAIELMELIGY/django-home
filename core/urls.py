from django.urls import path, include
from . import views





urlpatterns = [
	path('', views.home, name="home"),
	path('productHdl/',views.productHdl,name='productHdl'),
	path('productHdl/buspro/',views.buspro,name='buspro'),
	path('productHdl/knx/',views.knx,name='knx'),
	path('productHdl/product/<slug:slug>/',views.product_details,name="product"),
	path('tag/',views.tag,name="tag"),
	path('tag/<slug:slug>/',views.tag_details,name="tag"),
	path('tag/product/<slug:slug>/',views.producttuya_details,name="tuya")
]