import json
from functools import wraps

import jsonschema

ingredient_schema = {
    'properties': {
        'main_name': {'type': 'string', 'minLength': 3, 'maxLength': 50},
        'description': {'type': 'string', 'minLength': 10},
        'ingredient_type': {'type:': 'string', 'minLength': 5, 'maxLength': 50},
        'natural': {'type': 'boolean'},
        'hypoallergenic': {'type': 'boolean'},
        'related_names': {
            'type': 'array',
            'items': {'type': 'string', 'minLength': 3, 'maxLength': 50},
        },
    },
    "required": [
        "main_name",
        "description",
        "ingredient_type",
        "natural",
        "hypoallergenic",
    ],
}


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
