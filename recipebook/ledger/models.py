from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def biolength_validation(value):
    if len(value) < 255:
        raise ValidationError(
            _("%(value)s is too short. Minimum length is 255 characters."),
            params={"value": value},
        )


class Profile (models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    short_bio = models.TextField(validators=[biolength_validation])


class Ingredient(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('ledger:ingredient-detail', args=[self.pk])


class Recipe(models.Model):
    name = models.CharField(max_length=50)
    author = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name='recipes')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('ledger:recipe-detail', args=[self.pk])


class RecipeIngredient(models.Model):
    quantity = models.CharField(max_length=100)
    ingredient = models.ForeignKey(
        Ingredient, on_delete=models.CASCADE, related_name='recipe'
    )
    recipe = models.ForeignKey(
        Recipe, on_delete=models.CASCADE, related_name='ingredients'
    )

    def __str__(self):
        return f"{self.quantity} of {self.ingredient.name}"


class RecipeImage(models.Model):
    image = models.ImageField(upload_to='recipe_images/', blank=False)
    description = models.CharField(max_length=255, blank=True)
    recipe = models.ForeignKey(
        Recipe, on_delete=models.CASCADE, related_name='images'
    )

    def __str__(self):
        return f"Image for {self.recipe.name}: {self.description}"
