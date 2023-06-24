from django.urls import path
from .views import city_to_latlng, search_query_list , weather_detail
from django.contrib.auth import views as auth_views
from .views import signup,signin

urlpatterns = [
    path('city-to-latlng', city_to_latlng, name='city_to_latlng'),
    path('', city_to_latlng, name='home'),
    path('weather/<int:pk>/', weather_detail, name='weather_detail'),
    # histryview
    path('history/', search_query_list, name='history'),
    
    # account setup
    path('login/', signin, name='signin'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', signup, name='signup'),
]

