
from django.contrib import admin
from django.urls import path,include

# add path to admin
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('weatherApp.urls')),
]
