
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('app-birra/', include('AppBirra.urls')),
        
]
