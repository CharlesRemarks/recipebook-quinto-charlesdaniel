from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Recipe


class RecipeListView(ListView):
    model = Recipe
    template_name = 'ledger/recipes_list.html'


class RecipeDetailView(LoginRequiredMixin, DetailView):
    model = Recipe
    template_name = 'ledger/recipe_details.html'
    redirect_field_name = 'login.html'
