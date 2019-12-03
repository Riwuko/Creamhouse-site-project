from django.contrib import admin

from .models import (
    BodyCosmetic,
    CosmeticProperties,
    FaceCosmetic,
    FeetCosmetic,
    HairCosmetic,
    HandsCosmetic,
    Ingredient,
    IngredientName,
)

admin.site.register(BodyCosmetic)
admin.site.register(CosmeticProperties)
admin.site.register(FaceCosmetic)
admin.site.register(FeetCosmetic)
admin.site.register(HairCosmetic)
admin.site.register(HandsCosmetic)
admin.site.register(Ingredient)
admin.site.register(IngredientName)
