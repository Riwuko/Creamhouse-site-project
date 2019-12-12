"""creamhouse URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib.auth import views as auth_views
from django.urls import path

from cosmetics.views import (
    AddNewCosmetic,
    AddNewIngredient,
    CosmeticDetailView,
    CosmeticListView,
)
from cosmetics.views_api import CheckIngredient, FilterCosmetic


urlpatterns = [
    path('admin/', admin.site.urls),
    path('ingredient/add', AddNewIngredient.as_view()),
    path('cosmetic/add', AddNewCosmetic.as_view()),
    path(
        'accounts/login/',
        auth_views.LoginView.as_view(template_name='cosmetic/login.html'),
        name='login',
    ),
    path(
        'accounts/password-reset',
        auth_views.PasswordResetView.as_view(),
        name='password_reset',
    ),
    path(
        'accounts/password-done',
        auth_views.PasswordResetDoneView.as_view(),
        name='password_reset_done',
    ),
    path('ingredient/check/name', CheckIngredient.as_view()),
    path('cosmetic', CosmeticListView.as_view()),
    path('cosmetic/show/<pk>', CosmeticDetailView.as_view()),
    path('cosmetic/filter', FilterCosmetic.as_view()),
]
