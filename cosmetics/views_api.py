import json

from django.conf import settings
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.views import View

from cosmetics.models import Cosmetic, IngredientName


class CheckIngredient(View):
    def get(self, request):
        ingredient = request.GET.get('ingredient')
        names = list(
            IngredientName.objects.filter(
                name__istartswith=ingredient
            ).values_list('name', flat=True)[:5]
        )
        return JsonResponse({'ingredients': names})


class FilterCosmetic(View):
    def post(self, request):
        json_data = json.loads(request.body)
        current_page = json_data.get('page', 1)
        cosmetic_filter_data = json_data['cosmeticFilterData']
        filter_values = {
            key: value
            for key, value in cosmetic_filter_data.items()
            if value != 'all'
        }
        cosmetics_queryset = Cosmetic.objects.filter(**filter_values)
        paginator = Paginator(cosmetics_queryset, settings.PAGINATE_BY)
        paged_cosmetics = paginator.page(current_page)
        filtered_cosmetics = {
            'cosmetics': {
                cosmetic.pk: cosmetic.name for cosmetic in paged_cosmetics
            },
            'current_page': current_page,
            'previous_page': paged_cosmetics.previous_page_number()
            if paged_cosmetics.has_previous()
            else None,
            'next_page': paged_cosmetics.next_page_number()
            if paged_cosmetics.has_next()
            else None,
            'last_page': paginator.num_pages,
        }
        return JsonResponse(filtered_cosmetics)


class FilterIngredient(View):
    def post(self, request):
        json_data = json.loads(request.body)
        json_prepared = {
            f'ingredient__{key}': value
            for key, value in json_data.items()
            if value != 'all'
        }
        ingredient_queryset = IngredientName.objects.filter(**json_prepared)
        filtered_ingredients = {
            ingredient.pk: ingredient.name for ingredient in ingredient_queryset
        }
        return JsonResponse(filtered_ingredients)
