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
        return f'name: {self.name}'


class FaceCosmetic(models.Model):
    cosmetic = models.OneToOneField(
        Cosmetic, on_delete=models.CASCADE, primary_key=True
    )
    skin_type = models.CharField(max_length=2)
    time_of_day = models.CharField(max_length=1)
    properties = models.ManyToManyField(CosmeticProperties)

    def __str__(self):
        return f'cosmetic {self.cosmetic} skin_type: {self.skin_type}'


class HairCosmetic(Cosmetic, models.Model):
    cosmetic = models.OneToOneField(
        Cosmetic, on_delete=models.CASCADE, primary_key=True
    )
    hair_type = models.CharField(max_length=1)
    hair_problem = models.CharField(max_length=1)
    properties = models.ManyToManyField(CosmeticProperties)

    def __str__(self):
        return f'cosmetic {self.cosmetic}, hair_type: {self.hair_type}'


class BodyCosmetic(models.Model):
    cosmetic = models.OneToOneField(
        Cosmetic, on_delete=models.CASCADE, primary_key=True
    )
    skin_type = models.CharField(max_length=2)
    properties = models.ManyToManyField(CosmeticProperties)

    def __str__(self):
        return f'cosmetic {self.cosmetic}, skin_type: {self.skin_type}'


class FeetCosmetic(models.Model):
    cosmetic = models.OneToOneField(
        Cosmetic, on_delete=models.CASCADE, primary_key=True
    )
    skin_type = models.CharField(max_length=2)
    properties = models.ManyToManyField(CosmeticProperties)

    def __str__(self):
        return f'cosmetic {self.cosmetic}, skin_type: {self.skin_type}'


class HandsCosmetic(models.Model):
    cosmetic = models.OneToOneField(
        Cosmetic, on_delete=models.CASCADE, primary_key=True
    )
    skin_type = models.CharField(max_length=2)
    properties = models.ManyToManyField(CosmeticProperties)

    def __str__(self):
        return f'cosmetic {self.cosmetic}, skin_type: {self.skin_type}'


class Ingredient(models.Model):
    cosmetic = models.ManyToManyField(Cosmetic)
    description = models.TextField()
    ingredient_type = models.CharField(max_length=3)
    natural = models.BooleanField()
    hypoallergenic = models.BooleanField()
    verified = models.BooleanField(default=False)


class IngredientNames(models.Model):
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)


class Company(models.Model):
    name = models.CharField(max_length=120)
    website = models.URLField()
    country = models.CharField(max_length=2)

