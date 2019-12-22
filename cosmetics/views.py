from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render,redirect
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import DetailView, ListView, TemplateView

from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm

from cosmetics.json_schemas import (
    body_cosmetic_schema,
    face_cosmetic_schema,
    hair_cosmetic_schema,
    hands_feet_cosmetic_schema,
    ingredient_schema,
)
from cosmetics.models import (
    Cosmetic,
    BodyCosmetic,
    FaceCosmetic,
    FeetCosmetic,
    HairCosmetic,
    HandsCosmetic,
    Ingredient,
    IngredientName,
    CosmeticProperties,
)
from cosmetics.validation import validate_json


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'cosmetic/signup.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')


def homeView(request):
    return render(request, 'cosmetic/home.html',{})

# @method_decorator(login_required, name='dispatch')
class AddNewIngredient(View):
    def get(self, request):
        return render(request, 'cosmetic/ingredient_create.html', {})

    @method_decorator(validate_json(ingredient_schema))
    def post(self, request, requested_json):
        related_names = requested_json.pop('related_names')
        related_names.append(requested_json.pop('main_name'))
        ingredient = Ingredient(**requested_json)
        ingredient.save()
        IngredientName.objects.bulk_create(
            [
                IngredientName(name=name, ingredient=ingredient)
                for name in related_names
            ]
        )
        return JsonResponse({'message': ':)'})


class AddNewCosmetic(TemplateView):
    template_name = 'cosmetic/cosmetic_create.html'


class AddNewCosmeticType(View):
    model = None

    def post(self, request, requested_json):
        ingredients = requested_json.pop('ingredients')
        properties = requested_json.pop('properties')
        properties_objects = []
        for property_name in properties:
            obj, created = CosmeticProperties.objects.get_or_create(
                name=property_name
            )
            properties_objects.append(obj)
        ingredients_objects = []
        for ingredient in ingredients:
            ingredient_name_object=IngredientName.objects.get(name=ingredient)
            ingredients_objects.append(Ingredient.objects.get(pk=ingredient_name_object.pk))
        
        cosmetic = self.model(**requested_json)
        cosmetic.save()
        for property in properties_objects:
            cosmetic.properties.add(property)
        for ingredient in ingredients_objects:
            ingredient.cosmetic.add(cosmetic)
        return JsonResponse({'message': ':)'})


@method_decorator(validate_json(body_cosmetic_schema()), name='post')
class AddNewCosmeticBody(AddNewCosmeticType):
    model = BodyCosmetic


@method_decorator(validate_json(hands_feet_cosmetic_schema()), name='post')
class AddNewCosmeticHands(AddNewCosmeticType):
    model = HandsCosmetic


@method_decorator(validate_json(hands_feet_cosmetic_schema()), name='post')
class AddNewCosmeticFeet(AddNewCosmeticType):
    model = FeetCosmetic


@method_decorator(validate_json(hair_cosmetic_schema()), name='post')
class AddNewCosmeticHair(AddNewCosmeticType):
    model = HairCosmetic


@method_decorator(validate_json(face_cosmetic_schema()), name='post')
class AddNewCosmeticFace(AddNewCosmeticType):
    model = FaceCosmetic


class CosmeticListView(ListView):
    model = Cosmetic
    template_name = 'cosmetic/cosmetics_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_type'] = 'cosmetics'
        return context


class CosmeticDetailView(DetailView):
    model = Cosmetic
    template_name = 'cosmetic/cosmetics_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        properties = CosmeticProperties.objects.filter(
            cosmetic__name=self.object.name
        )
        context['properties'] = [property.name for property in properties]
        return context


class CosmeticCheckComposition(View):
    def get(self, request, pk):
        ingredients = Ingredient.objects.filter(cosmetic=pk)
        ingredients_names=[]
        for ingredient in ingredients:
            ingredient_names = IngredientName.objects.filter(ingredient=ingredient.pk)
            names = []
            for ingredient in ingredient_names:
                names.append(ingredient.name)
            ingredients_names.append(names)
        return JsonResponse(
            {
                'ingredients': [
                    {
                        'ingredient_names':ingredients_names[i],
                        'description': ingredient.description,
                        'ingredient_type': ingredient.ingredient_type,
                        'natural': ingredient.natural,
                        'hypoallergenic': ingredient.hypoallergenic,
                        'verified': ingredient.verified,
                    }
                    for i,ingredient in enumerate(ingredients)
                ]
            }
        )

class IngredientListView(ListView):
    model = IngredientName
    template_name = 'cosmetic/ingredients_list.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.distinct('ingredient')
        return queryset


class IngredientDetailView(DetailView):
    model = Ingredient
    template_name = 'cosmetic/ingredient_detail.html'

    def get_context_data(self, **kwargs):
        self.object = self.get_object()
        context = super().get_context_data(**kwargs)
        pk = self.object.pk
        ingredient_names = IngredientName.objects.filter(ingredient=pk).all()
        names = []
        for ingredient in ingredient_names:
            names.append(ingredient.name)
        print(names)
        context["ingredient_names"] = names
        return context
