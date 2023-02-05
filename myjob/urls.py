"""myjob URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('company/', include('company.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('area/', include('area.urls')),
    path('comment/', include('comment.urls')),
    path('company/', include('company.urls')),
    path('jobs/', include('jobs.urls')),
    path('resume/', include('resume.urls')),
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),
    path('center/<int:comments_user_pk>', views.center, name='center'),
    path('notifications/', include('notifications.urls', namespace='notifications')),
    path('my_notifications/', include('my_notifications.urls')),
    path('search/', views.search, name='search'),
    path('test/', views.test, name='test')
]
