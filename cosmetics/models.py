from django.db import models


class CosmeticProperties(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return f'name: {self.name}'


class Cosmetic(models.Model):
    name = models.CharField(max_length=30)
    target_gender = models.CharField(max_length=1)
    verified = models.BooleanField(default=False)

    def __str__(self):
        return f'cosmetic {self.name}'


class FaceCosmetic(Cosmetic):
    skin_type = models.CharField(max_length=2)
    time_of_day = models.CharField(max_length=1)
    properties = models.ManyToManyField(CosmeticProperties)


class HairCosmetic(Cosmetic):
    hair_type = models.CharField(max_length=1)
    hair_problem = models.CharField(max_length=1)
    properties = models.ManyToManyField(CosmeticProperties)


class BodyCosmetic(Cosmetic):
    skin_type = models.CharField(max_length=2)
    properties = models.ManyToManyField(CosmeticProperties)


class FeetCosmetic(Cosmetic):
    skin_type = models.CharField(max_length=2)
    properties = models.ManyToManyField(CosmeticProperties)


class HandsCosmetic(Cosmetic):
    skin_type = models.CharField(max_length=2)
    properties = models.ManyToManyField(CosmeticProperties)


class Ingredient(models.Model):
    main_name = models.CharField(max_length=50)
    cosmetic = models.ManyToManyField(Cosmetic, blank=True)
    description = models.TextField()
    ingredient_type = models.CharField(max_length=50)
    natural = models.BooleanField()
    hypoallergenic = models.BooleanField()
    verified = models.BooleanField(default=False)

    def __str__(self):
        return f'main name: {self.main_name}'


class IngredientName(models.Model):
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)


class Company(models.Model):
    name = models.CharField(max_length=120)
    website = models.URLField()
    country = models.CharField(max_length=2)
