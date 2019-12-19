import json
from django.http import JsonResponse
from functools import wraps
from cosmetics.json_schemas import *
import jsonschema

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

def validate_cosmetic_json(func):
    @wraps(func)
    def wrapper(request, *args, **kwargs):
        try:
            requested_cosmetics= json.loads(request.body)
            typ = requested_cosmetics['type']
            from pprint import pprint
            print('requested_cosmetics')
            pprint(requested_cosmetics)

            if (typ=="body"):
                body_schema = body_cosmetic_schema()
                jsonschema.validate(requested_cosmetics,body_schema)
            elif (typ=="hands" or typ=="feet"):
                hands_feet_schema = hands_feet_cosmetic_schema()
                jsonschema.validate(requested_cosmetics,hands_feet_schema)
            elif typ=="hair":
                hair_schema = hair_cosmetic_schema()
                print('hair_schema')
                pprint(hair_schema)
                jsonschema.validate(requested_cosmetics,hair_schema)
            elif typ=="face":
                face_schema = face_cosmetic_schema()
                jsonschema.validate(requested_cosmetics,face_schema)
            else:
                return JsonResponse(
                {'status': 400, 'error_message': 'wrong type'}, status=400)

            return func(
                *args,
                request=request,
                requested_cosmetics=requested_cosmetics,
                **kwargs
            )
        except jsonschema.exceptions.ValidationError as exc:
            error_message = exc.message
        except json.decoder.JSONDecodeError:
            error_message = 'Missing JSON in request.'
        print(error_message)
        return JsonResponse(
            {'status': 400, 'error_message': error_message}, status=400
        )

    return wrapper