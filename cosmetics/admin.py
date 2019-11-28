from django.contrib import admin

from .models import Cosmetic
from .models import HairCosmetic
from .models import FaceCosmetic
from .models import BodyCosmetic
# Register your models here.

admin.site.register(Cosmetic)
admin.site.register(HairCosmetic)