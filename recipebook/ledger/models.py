from django.db import models
from django.urls import reverse

class Ingredient(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('ledger:ingredient_detail', args=[str(self.pk)])

class Recipe(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('ledger:recipe_detail', args=[str(self.pk)])    
    

class RecipeIngredient(models.Model):
    quantity = models.CharField(max_length=30)

    Ingredient = models.ForeignKey(Ingredient,
                               on_delete=models.CASCADE,
                               related_name='ingredient')    
    
    recipe = models.ForeignKey(Recipe,
                               on_delete=models.CASCADE,
                               related_name='recipe')
    
    def __str__(self):
        return '{} - {} of {}'.format(self.recipe, self.quantity, self.Ingredient.name)