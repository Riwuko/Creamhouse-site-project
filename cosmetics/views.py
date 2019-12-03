import json
from functools import wraps

from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
import jsonschema
from django.utils.decorators import method_decorator

ingredient_schema = {"type": "array", "names": {"type": "string"}}


def validate_ingredients_json(func):
    @wraps(func)
    def wrapper(request, *args, **kwargs):
        try:
            requested_ingredients = json.loads(request.body)
            jsonschema.validate(requested_ingredients, ingredient_schema)
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
        return JsonResponse({'message': ':)'})
        # for i in range(len(requested_ingredients)):
        #     if i == 0:
        #         main_ingredient = Ingredients.objects.create(
        #             main_name=requested_ingredients[i]["name"]
        #         )
        #     else:
        #         IngredientNames.objects.create(
        #             main_ingredient, name=requested_ingredients[i]["name"]
        #         )
