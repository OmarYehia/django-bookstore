from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path("", views.index),
    path("<int:id>", views.singleResourceRud),
    path("login", obtain_auth_token),
    path("signup", views.api_signup)
]
