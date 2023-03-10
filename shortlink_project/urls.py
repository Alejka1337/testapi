"""shortlink_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken import views

from shortlink.views import shortlink_index, redirect_to_url
from shortlink.apiviews import CreateShortLink, UpdateShortLink, DetailShortLink


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/create-shortlink/', CreateShortLink.as_view()),
    path('api/shortlink/detail/<int:id>/', DetailShortLink.as_view()),
    path('api/shortlink/update/<int:id>/', UpdateShortLink.as_view()),
    path('api-auth/', include('rest_framework.urls')),
    path('api-token-auth/', views.obtain_auth_token),
    path('', shortlink_index),
    path('<str:short_link>/', redirect_to_url),
]
