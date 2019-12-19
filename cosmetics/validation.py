import json
from functools import wraps

import jsonschema
from django.http import JsonResponse


def validate_json(schema):
    def decorator(func):
        @wraps(func)
        def wrapper(request, *args, **kwargs):
            try:
                requested_json = json.loads(request.body)
                jsonschema.validate(requested_json, schema)
                return func(
                    *args,
                    request=request,
                    requested_json=requested_json,
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

    return decorator
