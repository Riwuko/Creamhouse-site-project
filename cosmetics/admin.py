from django.contrib import admin

from .models import (
    BodyCosmetic,
    FaceCosmetic,
    FeetCosmetic,
    HairCosmetic,
    HandsCosmetic,
)

admin.site.register(BodyCosmetic)
admin.site.register(FaceCosmetic)
admin.site.register(FeetCosmetic)
admin.site.register(HairCosmetic)
admin.site.register(HandsCosmetic)
