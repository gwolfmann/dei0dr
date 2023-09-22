from django.db import models

class AlimentType(models.Model):
    name = models.CharField(max_length=255)
    type_choices = [
        ('gluten', 'Gluten'),
        ('fat', 'Fat'),
        ('sodium', 'Sodium'),
        ('sugar', 'Sugar'),
        ('other', 'Other'),
    ]
    type = models.CharField(max_length=10, choices=type_choices, default='other')

    @classmethod
    def get_default_other_type(cls):
        return cls.objects.get(type='other')

class Ingredient(models.Model):
    name = models.CharField(max_length=255)
    types = models.ManyToManyField('AlimentType', default=AlimentType.get_default_other_type)
    
class IngredientInRecipe(models.Model):
    ingredient = models.ForeignKey('Ingredient', on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=10, decimal_places=3)
    measure_unit_choices = [
        ('kg', 'Kilogram'),
        ('lt', 'Liter'),
        ('gr', 'Gram'),
        ('unit', 'Unit'),
    ]
    measure_unit = models.CharField(max_length=10, choices=measure_unit_choices)

class Recipe(models.Model):
    name = models.CharField(max_length=255)
    ingredients = models.ManyToManyField('IngredientInRecipe')
    preparation = models.TextField()
