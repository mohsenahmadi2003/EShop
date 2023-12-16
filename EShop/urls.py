
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('home_module.urls')),
    path('contact/', include('contact_module.urls')),
    path('admin/', admin.site.urls),
    path('products/', include('product_module.urls')),
]
