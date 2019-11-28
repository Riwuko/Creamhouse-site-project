from django import forms

from .models import Cosmetic, HairCosmetic, FaceCosmetic, BodyCosmetic, Ingredient, IngredientNames

class CosmeticForm(forms.ModelForm):
	class Meta:
		model = Cosmetic
		fields = (
			'name',
			'target_gender'
		)

class HairCosmeticForm(CosmeticForm, forms.ModelForm):
	class Meta(CosmeticForm.Meta):
		model = HairCosmetic
		fields = CosmeticForm.Meta.fields + (
			'hair_type',
			'hair_problem',
			'properties'
		)

class FaceCosmeticForm(CosmeticForm,forms.ModelForm):
	class Meta(CosmeticForm.Meta):
		model = FaceCosmetic
		fields = CosmeticForm.Meta.fields + (
			'skin_type',
			'time_of_day',
			'properties'
		)

class BodyCosmeticForm(CosmeticForm,forms.ModelForm):
	class Meta(CosmeticForm.Meta):
		model = BodyCosmetic
		fields = CosmeticForm.Meta.fields + (
			'skin_type',
			'properties'
		)


class IngredientForm(forms.ModelForm):
	class Meta():
		model = Ingredient
		fields = (
			'ingredient_type',
			'natural',
			'hypoallergenic'
			)

class IngredientNamesForm(forms.ModelForm):
	class Meta():
		model = IngredientNames
		fields = (
			'name',
			)