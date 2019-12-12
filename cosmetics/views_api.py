from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views import View

from cosmetics.models import Cosmetic, IngredientName


class CheckIngredient(View):
    def get(self, request):
        ingredient = request.GET.get('ingredient')
        names = list(
            IngredientName.objects.filter(
                name__istartswith=ingredient
            ).values_list('name', flat=True)
        )
        return JsonResponse({'ingredients': names})


import json
class FilterCosmetic(View):
    def get(self, request):
        # j = json.loads(request.body)
        j = {
            'cosmetic_type': 'hair',
            'target_gender': 'Female',
            'haircosmetic__hair_type': 'high-porosity',
            'haircosmetic__hair_problem': 'colored',
        }
        d = Cosmetic.objects.filter(**j)
        print(d)
        return JsonResponse({})
