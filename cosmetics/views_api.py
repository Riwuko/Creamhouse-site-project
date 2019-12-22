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
    def post(self, request):
        json_data = json.loads(request.body)
        filter_values = {
            key: value for key, value in json_data.items() if value != 'all'
        }
        cosmetics_queryset = Cosmetic.objects.filter(**filter_values)
        filtered_cosmetics = {cosmetic.pk: cosmetic.name for cosmetic in cosmetics_queryset}
        return JsonResponse(filtered_cosmetics)
