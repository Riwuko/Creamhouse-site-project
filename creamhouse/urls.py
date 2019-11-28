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
from django.urls import path

from pages.views import home_view
from cosmetics.views import ProductCreateView, IngredientCreateView
from cosmetics.forms import HairCosmeticForm, FaceCosmeticForm, BodyCosmeticForm, IngredientForm

urlpatterns = [
	path('index/', home_view, name='home'),
    path('admin/', admin.site.urls),
    #path('product/', hair_detail_view),
 	path('createf/', ProductCreateView.as_view(form_class=FaceCosmeticForm)),
    path('create/', ProductCreateView.as_view(form_class=HairCosmeticForm)),
    path('createb/', ProductCreateView.as_view(form_class=BodyCosmeticForm)),
    path('createi/', IngredientCreateView.as_view()),


]