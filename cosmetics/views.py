from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View

from cosmetics.models import Ingredient, IngredientName
from cosmetics.validation import validate_ingredients_json


@method_decorator(login_required, name='dispatch')
class AddNewIngredient(View):
    def get(self, request):
        return render(request, 'cosmetic/ingredient_create.html', {})

    @method_decorator(validate_ingredients_json)
    def post(self, request, requested_ingredients):
        related_names = requested_ingredients.pop('related_names')
        ingredient = Ingredient(**requested_ingredients)
        ingredient.save()
        IngredientName.objects.bulk_create(
            [
                IngredientName(name=name, ingredient=ingredient)
                for name in related_names
            ]
        )
        return JsonResponse({'message': ':)'})


class AddNewCosmetic(View):
    def get(self, request):
        return render(request, 'cosmetic/cosmetic_create.html', {})

    def post(self, request):
        return JsonResponse({'message': ':)'})
