"""crime_report URL Configuration

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
from . import views
from location import views as location_views
from complaint import views as complaint_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name = 'home'),
    path('userhome/', views.userhome, name = 'userhome'),
    path('news/', views.feed, name = 'feed'),
    path('register/', views.registerpage, name = 'register'),
    path('login/', views.loginpage, name = 'login'),
    path('logout/', views.logoutUser, name='logout'),
    path('complaint/', complaint_views.comp, name = 'complaint'),
    path('status/', views.status, name = 'status'),
    path('location_search/', location_views.search, name='location'),
    path("location_map/<str:address>", location_views.map, name='map')
]
