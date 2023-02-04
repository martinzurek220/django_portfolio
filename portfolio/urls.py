"""portfolio URL Configuration

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
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from viewer.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', hello),
    # path('', prehled, name='prehled'),
    path('', PrehledView.as_view(), name='prehled'),
    path('grafy/', grafy, name='grafy'),
    # path('staking/', staking, name='staking'),
    path('farmy/', farmy, name='farmy'),
    path('ceny_tokenu/', ceny_tokenu, name='ceny_tokenu'),
    path('fast_api/', fast_api, name='fast_api'),
    path('system/', system, name='system'),
    path('staking/', staking, name='staking'),
]
