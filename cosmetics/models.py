from django.db import models
from multiselectfield import MultiSelectField

# Create your models here.
class Cosmetic(models.Model):
	name = models.CharField(max_length=30)

	F = 'F'
	M = 'M'
	B = 'B'

	GENDER_CHOICES = [
		(F, 'Female'),
		(M, 'Male'),
		(B, 'Both'),
	]

	target_gender = models.CharField(max_length=1, choices = GENDER_CHOICES)

	def __str__(self):
		return f'name: {self.name}'

class FaceCosmetic(Cosmetic,models.Model):
	OILY 	= 'Oi'
	DRY 	= 'Dr'
	SENS 	= 'Se'
	COMB 	= 'Co'
	NORM 	= 'No'
	CAPIL 	= 'Ca'

	SKIN_TYPE_CHOICES = [
		(OILY, 'Oily skin'),
		(DRY,  'Dry skin'),
		(SENS, 'Sensitive skin'),
		(COMB, 'Combination skin'),
		(NORM, 'Normal'),
		(CAPIL,'Capillaries')
	]

	DAY 	 = 'D'
	NIGHT 	 = 'N'

	TIME_OF_DAY_CHOICES = [
		(DAY,   'Day'),
		(NIGHT, 'Night'),
	]

	MOISTURIZING = 'M'
	REVIVISCENT  = 'R'
	ANTIAGING	 = 'A'
	CLEANSING 	 = 'C'
	SUNSCREEN	 = 'S'

	PROPERTIES_CHOICES = [
		(MOISTURIZING,  'Moisturizing'),
		(REVIVISCENT,	'Reviviscent'),
		(ANTIAGING,		'Antiaging'),
		(CLEANSING,		'Cleansing'),
		(SUNSCREEN, 	'Sunscreen'),
	]

	cosmetic 	= models.OneToOneField(Cosmetic, on_delete=models.CASCADE, primary_key=True)
	skin_type 	= models.CharField(max_length=2, choices = SKIN_TYPE_CHOICES)
	time_of_day = models.CharField(max_length=1, choices = TIME_OF_DAY_CHOICES)
	properties 	= MultiSelectField(choices = PROPERTIES_CHOICES,max_length=1)

	def __str__(self):
		return f'cosmetic {self.cosmetic} skin_type: {self.skin_type}'

class HairCosmetic(Cosmetic, models.Model):
	cosmetic 	= models.OneToOneField(Cosmetic, on_delete=models.CASCADE, primary_key=True)
	
	HIGH = 'H'
	LOW = 'L'
	MED = 'M'
	ALL = 'A'

	HAIR_TYPE_CHOICES = [
		(HIGH, 'High Porosity'),
		(LOW, 'Low Porosity'),
		(MED, 'Medium Porosity'),
		(ALL, 'All types'),
	]

	WEAK = 'H'
	COLORED = 'C'
	DANDRUFF = 'D'
	OILY = 'O'
	
	HAIR_PROBLEM_CHOICES = [
		(WEAK, 'Weak hair'),
		(COLORED, 'Colored hair'),
		(DANDRUFF, 'Dandruff hair'),
		(OILY, 'Oily hair'),
		(ALL, 'All hair'),
	]

	MOIS 		= 'MO'
	AG_GREAS 	= 'AG'
	COLOR_PRO	= 'CP'
	AG_HAIR_LOSS= 'HL'
	AG_DANDRUFF = 'AD'
	HAIR_GROWTH = 'HG'
	REVIV 		= 'RE'
	SMOOT 		= 'SM'

	PROPERTIES_CHOICES = [
		(MOIS,  'Moisturizing'),
		(AG_GREAS,'Against greasiness'),
		(COLOR_PRO, 'Color protection'),
		(AG_HAIR_LOSS, 'Against hair loss'),
		(AG_DANDRUFF, 'Against Dandrugg'),
		(HAIR_GROWTH, 'Hair growth'),
		(REVIV,	'Reviviscent'),
		(SMOOT, 'Smoothing')
	]

	hair_type 	= models.CharField(max_length=1, choices = HAIR_TYPE_CHOICES)
	hair_problem= models.CharField(max_length=1, choices = HAIR_PROBLEM_CHOICES)
	properties 	= models.CharField(max_length=2, choices = PROPERTIES_CHOICES)

	def __str__(self):
		return f'cosmetic {self.cosmetic}, hair_type: {self.hair_type},'

class BodyCosmetic(Cosmetic,models.Model):
	cosmetic 	= models.OneToOneField(Cosmetic, on_delete=models.CASCADE, primary_key=True)
	
	OILY = 'Oi'
	DRY = 'Dr'
	SENS = 'Se'

	SKIN_TYPE_CHOICES = [
		(OILY, 'Oily skin'),
		(DRY, 'Dry skin'),
		(SENS, 'Sensitive skin'),
	]

	MOISTURIZING = 'M'
	REVIVISCENT  = 'R'
	ANTIAGING	 = 'A'
	CLEANSING 	 = 'C'
	SUNSCREEN	 = 'S'

	PROPERTIES_CHOICES = [
		(MOISTURIZING,  'Moisturizing'),
		(REVIVISCENT,	'Reviviscent'),
		(ANTIAGING,		'Antiaging'),
		(CLEANSING,		'Cleansing'),
		(SUNSCREEN, 	'Sunscreen'),
	]

	skin_type 	= models.CharField(max_length=2, choices=SKIN_TYPE_CHOICES)
	properties 	= MultiSelectField(choices = PROPERTIES_CHOICES,max_length=1)


	def __str__(self):
		return f'cosmetic {self.cosmetic}, skin_type: {self.skin_type},'

class Ingredient(models.Model):
	cosmetic = models.ManyToManyField(Cosmetic)
	description = models.CharField(max_length=1000)

	PRES = 'PRE'
	EMO =  'EM0'
	EMU =  'EMU'
	EXT =  'EXT'
	SOLV=  'SOL'
	ANTIO ='ANT'
	CONS = 'CON'
	CHEL = 'CHE'
	FRAG = 'FRA'
	ANTIB ='ANT'
	PH_REG='PHR'
	VIT =  'VIT'
	SUNS=  'SUN'
	MOIS = 'MOI'
	CLEAN ='CLE'

	TYPE_CHOICES = [
		(PRES, 'Preservative'),
		(EMO, 'Emolient'),
		(EMU, 'Emulsifier'),
		(EXT, 'Extract'),
		(SOLV, 'Solvent'),
		(ANTIO, 'Antioxidant'),
		(CONS, 'Consistency'),
		(CHEL, 'Chelating'),
		(FRAG, 'Fragrance'),
		(ANTIB, 'Antibacterial'),
		(PH_REG, 'PH Regulator'),
		(VIT, 'Vitamin'),
		(SUNS, 'Sunscreen'),
		(MOIS, 'Moisturizing'),
		(CLEAN, 'Cleansing'),
	]

	ingredient_type = models.CharField(max_length=3, choices=TYPE_CHOICES)
	natural = models.BooleanField()
	hypoallergenic = models.BooleanField()

class IngredientNames(models.Model):
	ingredient 	= models.ForeignKey(Ingredient, on_delete=models.CASCADE, related_name='+')
	name = models.CharField(max_length=30)