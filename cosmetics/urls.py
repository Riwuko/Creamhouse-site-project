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
from django.urls import path

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
    IngredientDetailView,
    IngredientListView,
    Home,
)
from cosmetics.views_api import CheckIngredient, FilterCosmetic, FilterIngredient

app_name = 'cosmetics'

urlpatterns = [
    path('home', Home.as_view(), name='home'),
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
        'ingredient/check/name',
        CheckIngredient.as_view(),
        name='ingredient_check_name',
    ),
    path('cosmetic', CosmeticListView.as_view(), name='cosmetic'),
    path('cosmetic/filter', FilterCosmetic.as_view(), name='cosmetic_filter'),
    path('cosmetic/show/<int:pk>', CosmeticDetailView.as_view()),
    path(
        'api/cosmetic/<int:pk>/check-composition',
        CosmeticCheckComposition.as_view(),
    ),
    path('ingredient/add', AddNewIngredient.as_view(), name='ingredient_add'),
    path('ingredient', IngredientListView.as_view(), name='ingredient'),
    path('ingredient/filter', FilterIngredient.as_view(), name='ingredient_filter'),
    path('ingredient/show/<int:pk>', IngredientDetailView.as_view()),
]
