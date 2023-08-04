from django.shortcuts import render, redirect
from my_apps.recipes_app.models import Recipes
from my_apps.recipes_app.models import Comments
from .form import CommentsForm

# Create your views here.

def main_page(request):
    recipes = Recipes.objects.all()
    return render(request, 'index.html', {'recipes': recipes})


def single_recipe(request, recipe_id):
    recipe = Recipes.objects.get(pk=recipe_id)
    return render(request, 'single_recipe.html', context={'recipe': recipe})


def soup_page(request):
    soup = Recipes.objects.filter(food_type="soup")
    return render(request, 'soup_page.html', context={'soup': soup})
    

def dish_page(request):
    dish = Recipes.objects.filter(food_type='dish')
    return render(request, 'dish_page.html', context={'dish': dish})


def aperetize_page(request):
    aperetize = Recipes.objects.filter(food_type='aperetize')
    return render(request, 'aperetize_page.html', context={'aperetize': aperetize})


def drink_page(request):
    drink = Recipes.objects.filter(food_type='drink')
    return render(request, 'drink_page.html', context={'drink': drink})

def search_page(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        recipes = Recipes.objects.filter(name__contains=searched.upper())
        return render(request, 'search_page.html', {'searched': searched.upper(), 'recipes': recipes})
    else:
        return render(request, 'search_page.html', {})

def add_comments(request, pk):
    form = CommentsForm(request.POST)
    if form.is_valid():
        form = form.save(commit=False)
        form.recipe_id = pk
        form.save()
    return redirect(f'/{pk}')

def cookies(request):
    return render(request, 'cookies.html')