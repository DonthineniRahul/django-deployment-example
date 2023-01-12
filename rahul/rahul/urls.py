"""rahul URL Configuration

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
from django.conf.urls import url,include
from django.urls import path
from virat import views


# app_name = 'virat'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('virat/',views.index,name='sampu'),
    path('',include('virat.urls')),
    path('dilip/',views.vespa,name='vespa'),
    path('rahul/',views.thambi,name='dilip'),
    path('logout/',views.user_logout,name='logout'),
    path('special/',views.special,name='special'),
    # path('',views.kohli),
    # path('',views.form_name),
    # path('',views.users)
]
