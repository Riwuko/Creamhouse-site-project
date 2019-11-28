from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic

from .models import Ingredient, IngredientNames
from .forms import CosmeticForm, HairCosmeticForm, FaceCosmeticForm, BodyCosmeticForm, IngredientForm, IngredientNamesForm

# Create your views here.


class ProductCreateView(generic.edit.FormView):
	template_name = 'cosmetic/product_create.html'
	success_url='/index/'

	def form_valid(self, form):
		if form.is_valid():
			#HairCosmetic.objects.create(**form.cleaned_data)
			form.save()
		return super().form_valid(form)

class IngredientCreateView(generic.TemplateView):
	template_name = 'cosmetic/ingredient_create.html'
	ingredient_form_class = IngredientForm
	names_form_class = IngredientNamesForm

	def add(self,request):
		ingredient_data = request.POST or None
		ingredient_form = self.ingredient_form_class(ingredient_data, prefix='ingredient')
		names_form = self.names_form_class(ingredient_data, prefix='names')

		context = self.get_context_data(ingredient_form=ingredient_form, names_form=names_form)

		if ingredient_form.is_valid():
			self.form_save(ingredient_form)
		if names_form.is_valid():
			self.form_save(names_form)

		return self.render_to_response(context)

	def form_save(self,form):
		obj = form.save()
		message.success(self.request, "{} saved succesfully".format(obj))
		return obj

	def get(self,request, *args, **kwargs):
		return self.add(request, *args, **kwargs)