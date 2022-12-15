from rest_framework import routers
from rest_framework.authtoken import views

from django.urls import path, include


urlpatterns = [
    path('api-token-auth/', views.obtain_auth_token),

]
