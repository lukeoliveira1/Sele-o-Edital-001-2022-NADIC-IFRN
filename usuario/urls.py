from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from .views import *

app_name = 'usuario_urls'

urlpatterns = [
    path('login/', my_login ,name="login"),
    path('logout/', logout_request, name='logout'),
    path("registrar/", register, name="registrar")
]

