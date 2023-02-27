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
from django.urls import path, include

import api.views
from viewer.views import *
from accounts.views import SignUpView

from api.views import *

from rest_framework import *

from django.contrib.auth import views as auth_views

urlpatterns = [
    # App viewer
    path('admin/', admin.site.urls),
    path('hello/', hello),
    # path('', prehled, name='prehled'),
    path('', PrehledView.as_view(), name='prehled'),
    path('grafy/', grafy, name='grafy'),
    path('grafy/tabulky/', grafy_tabulky, name='grafy_tabulky'),
    # path('staking/', staking, name='staking'),
    path('farmy/', farmy, name='farmy'),
    path('ceny_tokenu/', ceny_tokenu, name='ceny_tokenu'),
    path('fast_api/', fast_api, name='fast_api'),
    path('system/', system, name='system'),
    path('staking/', staking, name='staking'),
    # path('settings/', settings, name='settings'),

    # App accounts
    # path('accounts/', include('accounts.urls')),
    path('accounts/signup/', SignUpView.as_view(), name='signup'),  # signup
    path('accounts/', include('django.contrib.auth.urls')),  # login, logout, password_change,...

    #App API
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/portfolio/', api.views.Portfolio.as_view({'get': 'list'})),
]
