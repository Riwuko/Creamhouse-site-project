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
from django.conf import settings
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import include, path

from cosmetics.views import (
    AddNewCosmetic,
    AddNewCosmeticBody,
    AddNewCosmeticFace,
    AddNewCosmeticFeet,
    AddNewCosmeticHair,
    AddNewCosmeticHands,
    AddNewIngredient,
    CosmeticCheckComposition,
    CosmeticDetailView,
    CosmeticListView,
    homeView,
    IngredientDetailView,
    IngredientListView,
    logout_view,
    signup,
)
from cosmetics.views_api import CheckIngredient, FilterCosmetic


urlpatterns = [
    path('admin/', admin.site.urls),
    path('ingredient/add', AddNewIngredient.as_view(), name='ingredient_add'),
    path('cosmetic/add', AddNewCosmetic.as_view(), name='cosmetic_add'),
    path(
        'cosmetic/add/body',
        AddNewCosmeticBody.as_view(),
        name='cosmetic_add_body',
    ),
    path(
        'cosmetic/add/face',
        AddNewCosmeticFace.as_view(),
        name='cosmetic_add_face',
    ),
    path(
        'cosmetic/add/feet',
        AddNewCosmeticFeet.as_view(),
        name='cosmetic_add_feet',
    ),
    path(
        'cosmetic/add/hands',
        AddNewCosmeticHands.as_view(),
        name='cosmetic_add_hands',
    ),
    path(
        'cosmetic/add/hair',
        AddNewCosmeticHair.as_view(),
        name='cosmetic_add_hair',
    ),
    path(
        'accounts/login/',
        auth_views.LoginView.as_view(template_name='cosmetic/login.html'),
        name='login',
    ),
    path(
        'accounts/signup/',
        signup,
        name='signup',
    ),
    path(
        'accounts/logout/',
        logout_view,
        name='logout',
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
    path(
        'home',
        homeView,
        name='home',
    ),
    path(
        'ingredient/check/name',
        CheckIngredient.as_view(),
        name='ingredient_check_name',
    ),
    path('cosmetic', CosmeticListView.as_view(), name='cosmetic'),
    path('cosmetic/show/<int:pk>', CosmeticDetailView.as_view()),
    path(
        'api/cosmetic/<int:pk>/check-composition',
        CosmeticCheckComposition.as_view(),
    ),
    path('cosmetic/filter', FilterCosmetic.as_view(), name='cosmetic_filter'),
    path('ingredient', IngredientListView.as_view(), name='ingredient'),
    path('ingredient/show/<int:pk>', IngredientDetailView.as_view()),
]


if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),

    ] + urlpatterns