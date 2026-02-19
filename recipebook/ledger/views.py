from django.views.generic import ListView, DetailView
from .models import Recipe

class RecipeListView(ListView):
    model = Recipe
    template_name = 'ledger/recipes_list.html'

class RecipeDetailView(DetailView):
    model = Recipe
    template_name = 'ledger/recipe_details.html'