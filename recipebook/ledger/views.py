from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from .forms import RecipeForm
from .models import Recipe


class RecipeListView(ListView):
    model = Recipe
    template_name = 'ledger/recipes_list.html'


class RecipeDetailView(LoginRequiredMixin, DetailView):
    model = Recipe
    template_name = 'ledger/recipe_details.html'
    redirect_field_name = 'login.html'


class RecipeCreateView(LoginRequiredMixin, CreateView):
    model = Recipe
    form_class = RecipeForm
    template_name = 'ledger/recipe_form.html'
    success_url = reverse_lazy('ledger:recipes-list')
