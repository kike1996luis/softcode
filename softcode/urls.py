from django.urls import path, include
from django.contrib import admin
from apps.products.views import ProductoListView, ProductoDetailView, ProductoCreateView

urlpatterns = [ 
    path("__reload__/", include("django_browser_reload.urls")),
    path('admin/', admin.site.urls),
    path('', ProductoListView.as_view(), name='producto_list'), 
    path('detalle/<int:pk>/', ProductoDetailView.as_view(), name='producto_detail'), 
    path('nuevo/', ProductoCreateView.as_view(), name='producto_create'), 
]