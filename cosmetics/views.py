import json
from functools import wraps

from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
import jsonschema
from django.utils.decorators import method_decorator

from cosmetics.models import Ingredient, IngredientName

ingredient_schema = {"type": "array", "names": {"type": "string"}}


def validate_ingredients_json(func):
    @wraps(func)
    def wrapper(request, *args, **kwargs):
        try:
            requested_ingredients = json.loads(request.body)
            # jsonschema.validate(requested_ingredients, ingredient_schema)
            return func(
                *args,
                request=request,
                requested_ingredients=requested_ingredients,
                **kwargs
            )
        except jsonschema.exceptions.ValidationError as exc:
            error_message = exc.message
        except json.decoder.JSONDecodeError:
            error_message = 'Missing JSON in request.'
        return JsonResponse(
            {'status': 400, 'error_message': error_message}, status=400
        )

    return wrapper


class AddNewIngredient(View):
    def get(self, request):
        context = {}
        return render(request, 'cosmetic/ingredient_create.html', context)

    @method_decorator(validate_ingredients_json)
    def post(self, request, requested_ingredients):
        print(requested_ingredients)
        # main_ingredient = Ingredient.objects.create(
        #     name=requested_ingredients[0]
        # )
        # main_ingredient.save()
        # related_ingredients = [
        #     IngredientName(ingredient=main_ingredient, name=name)
        #     for name in requested_ingredients[1:]
        # ]
        # IngredientName.objects.bulk_create(
        #     related_ingredients, ignore_conflicts=True
        # )
        return JsonResponse({'message': ':)'})


