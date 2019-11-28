from django.shortcuts import render
from django.views import View


class AddNewIngredient(View):
    def get(self, request):
        context = {}
        return render(request, 'cosmetic/ingredient_create.html', context)

