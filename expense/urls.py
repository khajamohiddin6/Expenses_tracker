from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),  # The route for the home page
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),  # Default login route
]
