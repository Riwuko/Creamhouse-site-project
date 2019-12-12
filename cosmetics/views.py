from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import DetailView, ListView

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
from cosmetics.validation import (
    validate_cosmetic_json,
    validate_ingredients_json,
)


@method_decorator(login_required, name='dispatch')
class AddNewIngredient(View):
    def get(self, request):
        return render(request, 'cosmetic/ingredient_create.html', {})

    @method_decorator(validate_ingredients_json)
    def post(self, request, requested_ingredients):
        related_names = requested_ingredients.pop('related_names')
        related_names.append(requested_ingredients.pop('main_name'))
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

    @method_decorator(validate_cosmetic_json)
    def post(self, request, requested_cosmetics):
        typ = requested_cosmetics['commonCosmeticData'].pop('type')
        ingredients = requested_cosmetics['commonCosmeticData'].pop(
            'ingredients'
        )
        name = requested_cosmetics['commonCosmeticData'].pop('name')
        target_gender = requested_cosmetics['commonCosmeticData'].pop(
            'target_gender'
        )
        description = requested_cosmetics['commonCosmeticData'].pop(
            'description'
        )
        properties = requested_cosmetics.pop('properties')
        requested_cosmetics.pop('commonCosmeticData')

        properties_objects = []
        for propertyName in properties:
            obj, created = CosmeticProperties.objects.get_or_create(
                name=propertyName
            )
            properties_objects.append(obj)
            print(obj.name)

        print(properties_objects)

        if typ == "body":
            cosmetic = BodyCosmetic(
                name=name,
                target_gender=target_gender,
                cosmetic_type=typ,
                **requested_cosmetics
            )
        elif typ == "hands":
            cosmetic = HandsCosmetic(
                name=name,
                target_gender=target_gender,
                cosmetic_type=typ,
                **requested_cosmetics
            )
        elif typ == "feet":
            cosmetic = FeetCosmetic(
                name=name,
                target_gender=target_gender,
                cosmetic_type=typ,
                **requested_cosmetics
            )
        elif typ == "hair":
            cosmetic = HairCosmetic(
                name=name,
                target_gender=target_gender,
                cosmetic_type=typ,
                **requested_cosmetics
            )
        elif typ == "face":
            cosmetic = FaceCosmetic(
                name=name,
                target_gender=target_gender,
                cosmetic_type=typ,
                **requested_cosmetics
            )
        else:
            return JsonResponse({'message': ':('})
        cosmetic.save()
        for propert in properties_objects:
            cosmetic.properties.add(propert)
        return JsonResponse({'message': ':)'})


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
